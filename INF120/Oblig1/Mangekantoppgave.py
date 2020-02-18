# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:50:14 2020

@author: Tor Erik


from turtle import *
forward(90)
left(45)
forward(80)

"""
#Her begynner oppgaven

from turtle import *
import time 

speed(10)
n = int(input("Hvor mange kanter skal mangekanten ha? "))


x=(360/n)

for m in range(0, n):
    forward(90)
    left(x)
    print("okok")

time.sleep(5)
#Blomstedelen 
clear()
antall_blader=int(input("Hvor mange blader skal blomsten ha? "))

mangekantsrotasjon=360/antall_blader

farge=['black', 'red', 'white' ]
t=[10, 3, 1]

for farge, t in zip(farge, t):
    pencolor(farge)
    pensize(t)
    for mangekant in range(antall_blader):
        for side in range(n):
            print(n)
            forward(100)
            right(x)
        right(mangekantsrotasjon)
    