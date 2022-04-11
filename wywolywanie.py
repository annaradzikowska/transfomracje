#!/usr/bin/python
# -*- coding: UTF-8 -*-
from math import radians
import numpy as np
import statistics as st


import sys
sys.path.append('C:\\Users\\Ania\\Desktop\\p1\\trans')
from trans import *
el_grs80 = Transformacje(model = "grs80")
plik = 'wsp_inp.txt'
# odczyt z pliku: https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.genfromtxt.html
tablica = np.genfromtxt(plik, delimiter=',', skip_header = 4)
# zapis: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.savetxt.html
#np.savetxt("wsp_out.txt", tablica, delimiter=',', fmt = ['%10.2f', '%10.2f', '%10.3f'], header = 'konversja współrzednych geodezyjnych \\ anna radzikowska')


tablica = np.genfromtxt(plik, delimiter=',', skip_header = 4)
rows,cols = np.shape(tablica)

hirvonen = np.zeros((rows,cols))
flh2xyz = np.zeros((rows,cols))
u2000 = np.zeros((rows,2))
u1992 = np.zeros((rows,2))
XYZ2elewacja = np.zeros((rows,2))


for i in range(rows):
    hirvonen[i] = el_grs80.hirvonen(tablica[i,0],tablica[i,1],tablica[i,2])
    flh2xyz[i] = el_grs80.flh2xyz(radians(hirvonen[i,0]),radians(hirvonen[i,1]),(hirvonen[i,2]))
    u2000[i] = el_grs80.u2000(radians(hirvonen[i,0]), radians(hirvonen[i,1]))
    u1992[i] = el_grs80.u1992(radians(hirvonen[i,0]), radians(hirvonen[i,1]))
    XYZ2elewacja[i]=el_grs80.XYZ2elewacja(tablica[i,0],tablica[i,1],tablica[i,2],radians(hirvonen[i,0]), radians(hirvonen[i,1]),hirvonen[i,2])



def main():
    plik = 'wsp_inp.txt'
    tablica = np.genfromtxt(plik, delimiter=',', skip_header = 4)
    while True:
        print('Wybierz tranformacje danych(wpisz odpowiednie cyfry po przecinku):')
        print('\t 1) Do układu współrzędnych krzywolinowych') #hirvonen
        print('\t 2) Do układu płaskiego 2000')               #u2000
        print('\t 3) Do układu płaskiego 1992')               #u1992
        print('\t 4) Do obliczenia azymutu i elewacji')       #XYZ2elewacja
        print('\t 5) Wyjście z programu')
        transformations = input('Wpisz cyfry odpowiadające wybranym transformacjom: ')
        if('1' in transformations):
            print("XYZ to fi lam h")
            for i in range (rows):
                print(hirvonen[i])
        elif('2' in transformations):
            print("Uklad 2000")
            for i in range (rows):
                print(u2000[i])
        elif('3' in transformations):
            print("Uklad 1992")
            for i in range (rows):
                print(u1992[i])
        elif('4' in transformations):
            print("XYZ 2 elewacja i azymut")
            for i in range (rows):
                print(XYZ2elewacja[i])
        elif('5' in transformations):
            return
        
            
if __name__ == '__main__':
    main() 
