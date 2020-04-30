import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
headers = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']



def extract_data(filename):
    df = pd.read_csv(filename, names=headers)

    sum = np.zeros(24)
    for i in range(24):
        sum[i] = np.sum(df[str(i)])

    data_depth = len(df['0'])
    data_temp = np.zeros(data_depth)



    for i in range(data_depth):
        for j in range(24):
            data_temp[i] += df[str(j)][i] / sum[j]

    data = data_temp / 24
    data_addup = np.zeros(data_depth)


    addup_start = 30
    data_addup[addup_start] = data[0]
    for i in range(data_depth - 1 - addup_start):
        data_addup[i + 1 + addup_start] = data_addup[i + addup_start] + data[i + 1]

    # data_addup[0] = data[0]
    # for i in range(data_depth-1):
    #     data_addup[i+1] = data_addup[i] + data[i+1]
    # print data
    # print data_addup



    print filename
    print "The percentage sum of final data:" ,
    print np.sum(data)
    print "The last addup data:" ,
    print data_addup[data_depth-1]
    return data,data_addup,data_depth

def combine_data(data_raw,combine_number,groupe_number):
    data = np.zeros(groupe_number)
    for i in range(groupe_number):
        for j in range(combine_number):
            data[i] += data_raw[(i*combine_number)+j]
    # print data_temp
    data_addup = np.zeros(groupe_number)
    addup_start= 150/(combine_number*5)
    print 'start number: ',
    print addup_start
    data_addup[addup_start] = data[0]
    for i in range(groupe_number-1-addup_start):
        data_addup[i+1+addup_start] = data_addup[i+addup_start] + data[i+1]


    print "The percentage sum of final combined data:" ,
    print np.sum(data)

    print "The last combined addup data:" ,
    print data_addup[groupe_number-1]
    return data,data_addup;




(data_200K,data_200K_addup,data_200K_depth) = extract_data('../../TDCV2_test/latency/200k_deadtime_500ns_latency.csv')
# print data_200K
print data_200K_depth
(data_400K,data_400K_addup,data_400K_depth) = extract_data('../../TDCV2_test/latency/400k_deadtime_500ns_latency.csv')
# print data_400K
print data_400K_depth





# X = np.arange(906)*5+150
#
# w=2.0
# plt.bar(X-w/2, data_200K*100,width=w,color='r',align='center',label='200K')
# plt.bar(X+w/2, data_400K*100,width=w,color='b',align='center',label='400K')
# plt.legend(frameon=False)
# plt.axis((-2,500,0,26))
# plt.savefig('latency_bar.png',dpi=300)
# plt.close()
#
#
# plt.plot(X, data_200K_addup*100,'o--',color='r',label='200K')
# plt.plot(X, data_400K_addup*100,'o--',color='b',label='400K')
# plt.legend(frameon=False)
# plt.axis((-2,500,0,105))
# plt.tight_layout()
# plt.savefig('latency_addup.png',dpi=300)
# plt.close()


###########################################################################################################################################################
X0 = np.arange(data_200K_depth)*5



plt.figure(figsize=(12, 5))
plt.yticks(np.arange(0, 1.01, step=0.1),['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(np.arange(0, 501, step=50))
plt.grid(color='grey', axis='y', linestyle='dashed')
plt.plot(X0, data_200K_addup,'x-',color='#71BC00',label='200K',markerfacecolor='none')
plt.plot(X0, data_400K_addup,'*-',color='#5218D8',label='400K',markerfacecolor='none')

# plt.legend(frameon=False)
leg = plt.legend( )

plt.axis((0,500,0,1.02))
plt.xlabel('Latency (ns)',size=15)
plt.ylabel('Percentage',size=15)

plt.savefig('latency_addup.png',dpi=300)
plt.close()
###########################################################################################################################################################
X1 = np.arange(data_400K_depth)*5+150
w=1.5
seperate= 0.65

plt.figure(figsize=(12, 5))
plt.yticks(np.arange(0, 1.01, step=0.1),['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(np.arange(0, 501, step=50))
plt.grid(color='grey', axis='y', linestyle='dashed')
plt.bar(X1-w*seperate, data_200K,width=w,color='#71BC00',align='center',label='200K',zorder=2,edgecolor='k')
plt.bar(X1+w*seperate, data_400K,width=w,color='#5218D8',align='center',label='400K',zorder=2,edgecolor='k')
# plt.legend(frameon=False)
leg = plt.legend( )

plt.axis((0,500,0,0.3))
plt.xlabel('Latency (ns)',size=15)
plt.ylabel('Percentage',size=15)

plt.savefig('latency_bar.png',dpi=300)
plt.close()


group_number = data_200K_depth / 5
(combined_data_200K,combined_data_200K_addup) = combine_data(data_200K,5,group_number)
(combined_data_400K,combined_data_400K_addup) = combine_data(data_400K,5,group_number)



###########################################################################################################################################################
X0 = np.arange(group_number)*25



plt.figure(figsize=(12, 5))
plt.yticks(np.arange(0, 1.01, step=0.1),['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(np.arange(0, 501, step=50))
plt.grid(color='grey', axis='y', linestyle='dashed')
plt.plot(X0, combined_data_200K_addup,'x-',color='#71BC00',label='200K',markerfacecolor='none')
plt.plot(X0, combined_data_400K_addup,'*-',color='#5218D8',label='400K',markerfacecolor='none')

plt.legend(frameon=False)
# leg = plt.legend( )

plt.axis((0,500,0,1.02))
plt.xlabel('Latency (ns)',size=15)
plt.ylabel('Integrated Percentage',size=15)

plt.savefig('latency_addup_combined.png',dpi=300)
plt.close()
###########################################################################################################################################################
X1 = np.arange(group_number)*25+150
w=7
seperate= 0.65

plt.figure(figsize=(12, 5))
plt.yticks(np.arange(0, 1.01, step=0.1),['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(np.arange(0, 501, step=50))
plt.grid(color='grey', axis='y', linestyle='dashed')
plt.bar(X1-w*seperate, combined_data_200K,width=w,color='#71BC00',align='center',label='200K',zorder=2,edgecolor='k')
plt.bar(X1+w*seperate, combined_data_400K,width=w,color='#5218D8',align='center',label='400K',zorder=2,edgecolor='k')
plt.legend(frameon=False)
# leg = plt.legend( )

plt.axis((0,500,0,0.8))
plt.xlabel('Latency (ns)',size=15)
plt.ylabel('Percentage',size=15)

plt.savefig('latency_bar_combined.png',dpi=300)
plt.close()



X0 = np.arange(group_number)*25



plt.figure(figsize=(12, 5))
plt.yticks(np.arange(0, 1.01, step=0.1),['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(np.arange(0, 601, step=50))
plt.grid(color='grey', axis='y', linestyle='dashed')
plt.plot(X0, 1-combined_data_200K_addup,'x-',color='#71BC00',label='200K',markerfacecolor='none')
plt.plot(X0, 1-combined_data_400K_addup,'*-',color='#5218D8',label='400K',markerfacecolor='none')
plt.yscale('log',basey=10)
plt.legend(frameon=False)
# leg = plt.legend( )

plt.xlim(0,600)
plt.ylim(10**(-9),2)
plt.xlabel('Latency (ns)',size=15)
plt.ylabel('Residual Percentage',size=15)

plt.savefig('latency_addup_combined_log.png',dpi=300)
plt.close()