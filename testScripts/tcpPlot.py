#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig1 = plt.figure()

data = pd.read_csv("../measurements/csv/tcpSpeedTest.csv",sep=',')

data = data.drop(['iter'],axis = 1)

tcp = data['version'] == 'tcp'
data1 = data[tcp]

quic = data['version'] == 'quic'
data2 = data[quic]

x = [1, 2, 3, 4]
file_sizes = ['file_1MB', 'file_100MB', 'file_250MB', 'file_500MB']

l = []
errors = []
for i in ['tcp']:
    yi = []
    ei = []
    for file in file_sizes:
        if file == 'file_1MB' : 
            s = 1
        if file == 'file_100MB':
            s = 100
        if file == 'file_250MB':
            s = 250
        if file == 'file_500MB':
            s = 500
        size = data['file'] == file
        data_i = (data[size]['version'] == i)
        yi.append(s/data[size][data_i]['time_total'].mean())
        ei.append(data[size][data_i]['time_total'].std())
    l.append(yi)
    errors.append(ei)

y1 = np.array(l[0])
e1 = np.array(errors[0])

# plt.yscale('log')
plt.plot(x, y1,color="blue", linewidth=1.0, linestyle='-', marker='*')
# plt.errorbar(x,y1,e1,linestyle='None', marker='.')
plt.xlabel('File Size')
plt.ylabel('Speed MB/s')
plt.ylim(ymin=0)
# Donner un titre à votre graphe.
plt.title("TCP's average speed for different file sizes")

# Permet d'ajouter une grille au graphe, rendant la lecture de vos données plus facile.
plt.grid(True)
plt.legend(['TCP'], loc = 'upper left')
plt.xticks(x,file_sizes)

plt.show()

size = data['file'] == 'empty_file'
print(size)
data_i = (data[size]['version'] == i)
print(data[size][data_i]['time_total'].mean())

print("The end")