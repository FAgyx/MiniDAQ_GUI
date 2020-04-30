import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from operator import add
headers = ['ChnlID','EdgeType','Bin0','Bin1','Bin2','Bin3']



ID_number = []

df = pd.read_csv('../chip8/run_binsize.csv', names=headers,usecols=[0,2,3,4,5,6])
# with df['Binl'] as data_point :
#     print data_point
ChnlID = df['ChnlID']
EdgeType = df['EdgeType']
Bin0=df['Bin0']
Bin1=df['Bin1']
Bin2=df['Bin2']
Bin3=df['Bin3']
for i in range(48):
    ID_number.append(int(ChnlID[i])*2 + 1 + (1 if EdgeType[i]=="f" else 0))


plt.figure(figsize=(10, 5))

plt.plot(ID_number, Bin0, 'bs',markersize=3,label='Bin 0')
plt.plot(ID_number, Bin1, 'go',markersize=3,label='Bin 1')
plt.plot(ID_number, Bin2, '^',markersize=3,label='Bin 2')
plt.plot(ID_number, Bin3, "D",markersize=3,label='Bin 3')

plt.plot([0, 49], [781.25, 781.25], 'r--')
plt.plot([0, 49], [781.25+40, 781.25+40], '--',color='grey')
plt.plot([0, 49], [781.25-40, 781.25-40], '--',color='grey')

plt.legend(frameon=False)

plt.axis((0,49,650,900))
# plt.text(25,875,'MDT_TDC_Ver1 Bin Size v.s. Channel',horizontalalignment='center',size=15)
plt.text(5,785,'781.25 ps',horizontalalignment='center',size=10,color='red',fontweight='bold')
plt.text(5,773+52,'+40 ps',horizontalalignment='center',size=10,color='red',fontweight='bold')
plt.text(5,773-42,'-40 ps',horizontalalignment='center',size=10,color='red',fontweight='bold')

# plt.title('MDT_TDC_Ver1 Bin Size v.s. Channel')
plt.xlabel('Channel (1-48, 24 channels x 2 edges)',size=15)
plt.ylabel('Bin Size (ps)',size=15)

plt.savefig('../chip8/chip8_binsize.png',dpi=300)
# plt.show()

binsize = 781.25
DNL0 = [data-binsize for data in Bin0]
DNL1 = [data-binsize for data in Bin1]
DNL2 = [data-binsize for data in Bin2]
DNL3 = [data-binsize for data in Bin3]
DNL_list = list(zip(DNL0,DNL1,DNL2,DNL3))
INL_list = [[data[0],data[0]+data[1],data[0]+data[1]+data[2],
             data[0]+data[1]+data[2]+data[3]] for data in DNL_list]
x=[0,1,2,3]
plt.figure(figsize=(7.1, 4))
for i in range(48):
    plt.plot(x, DNL_list[i], 'ko-',linewidth=0.5,markersize=2,mew=0,mfc='r')
plt.axis((0,3,-45,45))
plt.xlabel('TDC Bin',size=10)
plt.ylabel('DNL (ps)',size=10)
plt.savefig('../chip8/chip8_bin_DNL.png',dpi=300)
# plt.show()
plt.figure(figsize=(7.1, 4))
for i in range(48):
    plt.plot(x, INL_list[i], 'ko-',linewidth=0.5,markersize=3,mew=0,mfc='r')
plt.axis((0,3,-30,50))
plt.xlabel('TDC Bin',size=10)
plt.ylabel('INL (ps)',size=10)
plt.savefig('../chip8/chip8_bin_INL.png',dpi=300)
# plt.show()


# best straight line fit not suitable for TDC
# y0 = [data for data in Bin0]
# y1 = list(map(add,y0,[data for data in Bin1]))
# y2 = list(map(add,y1,[data for data in Bin2]))
# y3 = list(map(add,y2,[data for data in Bin3]))
#
# y_list = list(zip(y0,y1,y2,y3))
# x_list = [0,1,2,3]
# x = np.array(x_list)
# INL_list = []
# for i in range(len(y_list)):
#     y=np.array(y_list[i])
#     z=np.polyfit(x,y,1)
#     INL_list.append([])
#     for j in range(len(y_list[i])):
#         INL_list[i].append(y_list[i][j]-(z[0]+z[1]*x_list[j]))
# plt.figure()
# for i in range(48):
#     plt.plot([0,1,2,3], INL_list[i], 'ko-',linewidth=0.5,markersize=3,mfc='r')
# plt.show()