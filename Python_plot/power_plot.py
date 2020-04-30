import matplotlib.pyplot as plt
import pandas as pd
from operator import itemgetter
import numpy as np

headers = ['ChipID','Power']

df = pd.read_csv('../powertest/power_test.csv', header=0,names=headers,usecols=[0,5])
chipID=df['ChipID']
power=df['Power']
power_list = []

for i in range(len(power)/4):
    power_list.append([])
    power_list[i].append(chipID[i*4])
    power_list[i].append(power[i*4+1])
    power_list[i].append(power[i*4+3])
    power_list[i].append((power[i*4+1]) + (power[i*4+3]))
power_list.sort(key=itemgetter(0))
plt.figure(figsize=(6, 4))
chip = [d[0] for d in power_list]
power_analog = [d[2] for d in power_list]
power_digital = [d[1] for d in power_list]
power_total = [d[3] for d in power_list]
# plt.plot([d[0] for d in power_list], [d[3] for d in power_list], 'r^',markersize=3,label='Total')
# plt.plot([d[0] for d in power_list], [d[1] for d in power_list], 'bs',markersize=3,label='Digital')
# plt.plot([d[0] for d in power_list], [d[2] for d in power_list], 'go',markersize=3,label='Analog')
width = 0.35
plt.bar(chip,power_analog,width, label='Analog')
plt.bar(chip,power_digital,width, bottom = power_analog, label='Digital')
plt.legend(frameon=True)
plt.ylim(0,350)
plt.xlabel('Chip ID',size=10)
plt.ylabel('Power (mW)',size=10)
power_total_array = np.array(power_total)
std = np.std(power_total_array)
mean = np.mean(power_total_array)
plt.text(4,320,'mean ='+str(mean)[0:5],horizontalalignment='center',size=10,color='black',fontweight='bold')
plt.text(4,300,'std  ='+str(std)[0:3],horizontalalignment='center',size=10,color='black',fontweight='bold')
# plt.savefig('../powertest/powertest.png',dpi=300)

power_analog_array = np.array(power_analog)
std = np.std(power_analog_array)
mean = np.mean(power_analog_array)
print("analog",mean,std)
power_digital_array = np.array(power_digital)
std = np.std(power_digital_array)
mean = np.mean(power_digital_array)
print("digital",mean,std)
plt.show()