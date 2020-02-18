# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:25:49 2020

@author: Tor Erik

#Money in the bank 100000$$
#renten er 3%

penger=10000
ønsket_saldo=50000
år=0
while penger <= ønsket_saldo:
    penger += 1000
    penger *= 1.03
    år += 1
print("Det tok ", år, "år for  å få over ", ønsket_saldo)

"""
penger=10000
ønsket_saldo=50000
år=0

while penger <= ønsket_saldo:
    år +=1
    penger += 1000
    if år<10:
        rente= 1.032
    else:
        rente = 1.03
    penger *= rente
    
print("Det tok ", år, "år for  å få over ", ønsket_saldo)
    
