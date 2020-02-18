# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:43:36 2020

@author: Tor Erik
"""

#Mangekant oppgave
from turtle import *

clear()
setx(0), sety(0)

pensize(5)
antall_sider=4
sidelengde=80
vinkel=360/antall_sider
farger=['red','blue','green','blue']
antall_farger=len(farger)

for side in range(antall_sider):
    pennefarge=farger[side % antall_farger]
    pencolor(pennefarge)
    forward(sidelengde)
    left(vinkel)
    