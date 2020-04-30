import matplotlib.pyplot as plt
import pandas as pd
import numpy as numpy
from operator import itemgetter
import csv
# headers = ['Count','Measured Interverl','Stdev','run name']
headers = ['Measured Interverl','Stdev']


def extract_data1(file_name):
    # print file_name
    x = []
    y = []
    df = pd.read_csv(file_name, names=headers,usecols=[4,5])
    x = [data for data in df['Measured Interverl']]
    y = [data/(2**0.5) for data in df['Stdev']]
    return x,y

def extract_data(file_name):
    # print file_name
    x = []
    y = []
    df = pd.read_csv(file_name, names=headers,usecols=[4,5])
    x = [data for data in df['Measured Interverl']]
    y = [data/(2**0.5) for data in df['Stdev']]
    x_y = list(zip(x,y))
    return x_y


plt.figure(figsize=(10, 5))
import glob
files = glob.glob("../chip8/time_res/*.csv")

diff0_headers = ['chnl1','chnl2','edge','mean','std']
df = pd.read_csv('../chip8/run_time_res_0diff.csv', names=diff0_headers, usecols=[0,1,2,4,5])
diff0_chnl1 = [data for data in df['chnl1']]
diff0_chnl2 = [data for data in df['chnl2']]
diff0_edge = [data for data in df['edge']]
diff0_mean = [data for data in df['mean']]
diff0_std = [data/(2**0.5) for data in df['std']]



# import itertools
# marker = itertools.cycle(('.', 'o', 'v', '^', '+','D','s','p', 'P','H','x','d'))

# for filenames in files:
#     x_y = extract_data(filenames)
#     chnl1 = int(filenames[-15:-13])
#     chnl2 = int(filenames[-8:-6])
#     edgetype = filenames[-5]
#     for i in range(48):
#         if ((diff0_chnl1[i]== chnl1 and diff0_chnl2[i] == chnl2) or\
#            (diff0_chnl1[i] == chnl2 and diff0_chnl2[i] == chnl1)) and\
#            diff0_edge[i] == edgetype:
#             x_y = [data for data in x_y if data[0]>0.010 or data[0]<-0.010]
#             x_y.append([diff0_mean[i], diff0_std[i]])
#             x_y.sort(key=itemgetter(0))
#     x = [data[0] for data in x_y]
#     y = [data[1] for data in x_y]
#
#     # plt.plot(x, y,'--' ,linewidth=1, c=numpy.random.rand(3),label='')linestyle = ''
#     plt.plot(x, y, 'o--', c=numpy.random.rand(3),label='',markersize=2)


(x, y) = extract_data1("../chip8/time_res/run_0204_chnl05_chnl18_r.csv")
plt.plot(x, y,'ro' ,linewidth=1,label='Data',markersize=3)

(x, y) = extract_data1("./theory.csv")
plt.plot(x, y,'k-' ,linewidth=1,label='Theoretical Prediction')

plt.legend(loc=1,frameon=False)


plt.xlabel('Delay (LSB)',size=15)
plt.ylabel('RMS precision (LSB)',size=15)

plt.axis((-1,1,0,0.45))

plt.savefig('../chip8/channel5_18_time_res.png',dpi=300)
plt.show()