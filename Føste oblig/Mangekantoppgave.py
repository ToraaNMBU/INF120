# -*- coding: utf-8 -*-
"""
# -*- coding: utf-8 -*-

_author_ Tor Erik Aasestad
_email_ toraa@nmbu.no


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

time.sleep(5)
#Blomstedelen 
clear()
antall_blader=int(input("Hvor mange blader skal blomsten ha? "))

mangekantsrotasjon=360/antall_blader

farge=['black', 'red', 'white' ]
t=[10, 3, 1]

for mangekant in range(antall_blader):
    for side in range(n):5
        forward(100)
        right(x)
    right(mangekantsrotasjon)
time.sleep(10)