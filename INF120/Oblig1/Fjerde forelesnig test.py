# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:22:32 2020

@author: Tor Erik
"""

list=[1,2,3,4]
for list in range(0,5):
    print(list)
    

#Navnelister
navneliste = ["Meg", "Deg", "oss"] 
for navn in navneliste:
		print("Hei ", navn)
print("Nå har jeg vært en flink datamaskin")
print("reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

#Navnelister
#For å telle igjennom lista bruker vi Range-funkjsonen 
navneliste=["Meg", "Deg", "oss", "alle"]
for navn_id in range(3):
	navn=navneliste[navn_id]
	print("Navn nummer", navn_id, "er ", navn) 

#En å oppdatrere lengden osv bruker vi følgende:
#For å telle igjennom lista bruker vi Range-funkjsonen 
navneliste=["Meg", "Deg", "oss", "alle"]
antall_navn=  len(navneliste) #Finner lengden på listen
for navn_id in range(antall_navn): 
	navn=navneliste[navn_id]
	print("Navn nummer", navn_id, "er ", navn) 




#    
navneliste=["Meg", "Deg", "oss", "alle"]
antall:_navn=len(navneliste)
for person.id, navn in zip(range(antall_navn), navneliste):
	print("Navn nummer", navn_id, "er ", navn) 



divisor=5
dividert=2
kvotient=0
rest=divisor
while rest>=dividert:
	kvotient= kvotient+1
	rest=rest-dividert
print(divisor, "Delt på ", dividert, "er", kvotient, "med en rest på ", rest)
	