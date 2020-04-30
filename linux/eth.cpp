/*******************************
 * Ethernet packet capture program
 * Liang Guan (guanl@umich.edu)
 * 18 May 2016
 * 
 * How to run
 * $g++ eth.cpp -lpcap -o mac_daq
 *****************************/

#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <string>

#include <signal.h>  /*for signal() and raise()*/
#include <pcap.h>  
#include <errno.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>



using namespace std;

/* Define global variables to manipulate data */ 
pcap_t *pcap_handle;
char *dev;  //device name
char err_buf[PCAP_ERRBUF_SIZE]; 

char packet_filter[]="ether src 07:08:09:0a:0b:0c"; //filter expression
struct bpf_program fcode; // compile filter program  
bpf_u_int32 netmask=0xffffff; //

struct pcap_pkthdr* header;//
const u_char *pkt_data;//

string run_name;
bool daq_stop=false;

void signalHandler (int signum){
   daq_stop=true;
   cout<<"DAQ stopped!! --"<<signum<<endl;
}




/* create a file to save captured data*/ 
FILE *fp;

void got_packet(u_char *useless, const struct pcap_pkthdr* pkthdr, const u_char* packet_data)
{
        fwrite(packet_data,(pkthdr->len),1,fp);
}

int packet_receiver(){

    int ret=0;
    int fd=0;   //define a file descriptor 
    fd_set rfds; //file descriptor sets for "select" function (it's a bit arrray)
    struct timeval tv;  // strcuture represents elapsed time (declared in sys/time.h)
    const int TIMEOUT=60;  //timeout in seconds

    fd=pcap_fileno(pcap_handle); //pcap_fileno returns the descriptor for the packet capture device
    FD_ZERO(&rfds);   //re-clears(empty) file descriptor set 
    FD_SET(fd,&rfds); //rebuild file descriptor set
    
    tv.tv_sec=TIMEOUT;
    tv.tv_usec=0;
 
    ret=select(fd+1, &rfds, NULL, NULL, &tv); 
    //select(): blocks the calling process until there is activity on file descriptor set or until the timeout period has expired
 
    if(-1==ret) cout<<"Select failed"<<endl;
    else if(ret){
        pcap_dispatch(pcap_handle,1, got_packet,NULL);
    }else{
        //#ifdef DEBUG
                cout<<"Select timeout on fd:"<<fd<<" Return code: "<<ret<<endl;
        //#endif
    }

    return ret;
}


int main(int argc, char **argv)
{

    /* get run number*/
    int iPacket=0;  //packet counter
    string run_id;
    string verbose;
    if (argc!=4){cout<<"Usage: sudo ./mac_daq run_name -verbose on/off"<<endl; return 0;}
    else {
	run_id=argv[1];
	verbose=argv[3];
	run_name="run_"+run_id+".bin";
	cout<<"run_name is: "<<run_name<<endl;
    }

 
    /* prepare run: open file, get run pid, declare signal slot*/
    fp=fopen(run_name.c_str(),"wb");//
    signal(SIGUSR1,signalHandler);

    ofstream fpid("current_run_meta.dat");
    fpid<<getpid()<<endl;
    cout<<"run pid is: "<<getpid()<<endl;


    pcap_if_t *alldevs;
    pcap_if_t *d;
    int i = 0;

    if (pcap_findalldevs( &alldevs, err_buf) == -1)
    {
        cerr <<"Error in pcap_findalldevs_ex:"<< err_buf << endl;
        exit(1);
    }
    for(d= alldevs; d != NULL; d= d->next)
    {
        cout << ++i << ":"<< d->name <<"    ";
        if (d->description)
            cout << d->description << endl;
        else
            cout<< "(No description available)" << endl;
    }
    int device_number;
    cout << "plese select your etherner device: ";
    cin >> device_number;
    d= alldevs;
    for(i=0; i < device_number -1; i++){
        d=d->next;        
    }
    cout << ++i << ":"<< d->name <<"    ";
    if (d->description)
        cout << d->description << endl;
    else
        cout<< "(No description available)" << endl;


    /* open the ethernet device*/
    //dev = pcap_lookupdev(err_buf);
    //if (dev==NULL){
    //    cout<<"Could not find device "<<dev<<" : "<<err_buf<<endl;
    //    return -1;
    //}else{
	//printf("Found Device %s\n",dev);
    //}
    dev = d->name;
    pcap_handle = pcap_open_live(dev,65536,1,10000, err_buf);  //device name, snap length, promiscuous mode, to_ms, error_buffer
    if (pcap_handle==NULL){
        cout<<"Could not open device "<<dev<<" : "<<err_buf<<endl;
	return -1;
    }

    /* compile the filter */
    if (pcap_compile(pcap_handle, &fcode, packet_filter, 1, netmask) < 0){
	    cout<<"Unable to compile the packet filter. Check the syntax!"<<endl;
            pcap_close(pcap_handle);
            return -1;
    }

    /* apply filter*/ 
    if (pcap_setfilter(pcap_handle, &fcode) < 0){
	    cout<<"Filter address error. Can not apply filter!"<<endl;
            pcap_close(pcap_handle);
            return -1;
    }

    /* sniff data packets*/
    //while(packet_receiver()!=0&&iPacket<N_PACKET)
    while(packet_receiver()!=0 && daq_stop==false)
    {
	   ++iPacket;
	   if(verbose=="on") cout<<"Packet #"<<iPacket<<endl;
    }

    /* clean up and close pcap */
    pcap_freealldevs(alldevs);
    pcap_freecode(&fcode);
    pcap_close(pcap_handle);
    fclose(fp);
	

}
