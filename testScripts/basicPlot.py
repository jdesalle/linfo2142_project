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

x = [1, 2, 3, 4, 5, 6]
file_sizes = ['empty_file', 'file_100MB', 'file_1MB', 'file_250MB', 'file_500MB']
mesurements = ['time_namelookup','time_connect','time_appconnect','time_pretransfer','time_starttransfer','time_total']

l = []
errors = []
for i in ['tcp', 'quic']:
    yi = []
    ei = []
    size = data['file'] == 'empty_file'
    print(size)
    data_i = (data[size]['version'] == i)
    yi.append(data[size][data_i]['time_namelookup'].mean())
    yi.append(data[size][data_i]['time_connect'].mean())
    yi.append(data[size][data_i]['time_appconnect'].mean())
    yi.append(data[size][data_i]['time_pretransfer'].mean())
    yi.append(data[size][data_i]['time_starttransfer'].mean())
    yi.append(data[size][data_i]['time_total'].mean())
    ei.append(data[size][data_i]['time_namelookup'].std())
    ei.append(data[size][data_i]['time_connect'].std())
    ei.append(data[size][data_i]['time_appconnect'].std())
    ei.append(data[size][data_i]['time_pretransfer'].std())
    ei.append(data[size][data_i]['time_starttransfer'].std())
    ei.append(data[size][data_i]['time_total'].std())
    l.append(yi)
    errors.append(ei)

y1 = np.array(l[0])
y2 = np.array(l[1])
e1 = np.array(errors[0])
e2 = np.array(errors[1])

# plt.yscale('log')
plt.plot(x, y1,color="blue", linewidth=1.0, linestyle='None', marker='*')
plt.errorbar(x,y1,e1,linestyle='None', marker='.')
plt.plot(x, y2,color="red", linewidth=1.0, linestyle='None', marker='*')
plt.errorbar(x,y2,e2,linestyle='None',marker='.')
plt.xlabel('Variable')
plt.ylabel('Duration [s]')
plt.ylim(ymin=0)
# Donner un titre à votre graphe.
plt.title("TCP vs QUIC")

# Permet d'ajouter une grille au graphe, rendant la lecture de vos données plus facile.
plt.grid(True)

# Ajouter une légende, loc peut prendre différentes valeurs (https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html)

plt.legend(['TCP','QUIC'], loc = 'upper left')
plt.xticks(x,mesurements, rotation='vertical')

plt.show()

print("The end")