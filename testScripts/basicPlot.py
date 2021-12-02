#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig1 = plt.figure()

#data = pd.read_csv("testAndSet.csv",sep=',')
#data = pd.read_csv("philo.csv",sep=',')
#data = pd.read_csv("prodCons.csv",sep=',')
#data = pd.read_csv("readWrite.csv",sep=',')
data = pd.read_csv("basicSpeedTest.csv",sep=',')

data = data.drop(['iter'],axis = 1)


tcp = data['version'] == 'tcp'
data1 = data[tcp]

quic = data['version'] == 'quic'
data2 = data[quic]

x = [1, 2, 3, 4, 5]
file_sizes = ['empty_file', 'file_100MB', 'file_1MB', 'file_250MB', 'file_500MB']

l = []
errors = []
for i in ['tcp', 'quic']:
    yi = []
    ei = []
    for file in ['empty_file', 'file_100MB', 'file_1MB', 'file_250MB', 'file_500MB']: #nbr de thread
        size = data['file'] == file
        print(size)
        data_i = (data[size]['version'] == i)
        yi.append(data[size][data_i]['time_total'].mean())
        ei.append(data[size][data_i]['time_total'].std())
        # yi.append(data[size][data_i]['time_connect'].mean())
        # ei.append(data[size][data_i]['time_connect'].std())
        # yi.append(data[size][data_i]['time_appconnect'].mean())
        # ei.append(data[size][data_i]['time_appconnect'].std())
        # yi.append(data[size][data_i]['time_starttransfer'].mean())
        # ei.append(data[size][data_i]['time_starttransfer'].std())
        # yi.append(data[size][data_i]['time_namelookup'].mean())
        # ei.append(data[size][data_i]['time_namelookup'].std())
    l.append(yi)
    errors.append(ei)

y1 = np.array(l[0])
y2 = np.array(l[1])
e1 = np.array(errors[0])
e2 = np.array(errors[1])

# plt.yscale('log')
plt.plot(x, y1,color="blue", linewidth=1.0, linestyle="-")
plt.errorbar(x,y1,e1,linestyle='None', marker='.')
plt.plot(x, y2,color="red", linewidth=1.0, linestyle="-")
plt.errorbar(x,y2,e2,linestyle='None',marker='.')
plt.xlabel('File size')
plt.ylabel('total time [s]')
plt.ylim(ymin=0)
# Donner un titre à votre graphe.
plt.title("TCP vs QUIC")

# Permet d'ajouter une grille au graphe, rendant la lecture de vos données plus facile.
plt.grid(True)

# Ajouter une légende, loc peut prendre différentes valeurs (https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html)

plt.legend(['TCP','QUIC'], loc = 'upper right')
plt.xticks(x,file_sizes)

plt.show()

print("The end")