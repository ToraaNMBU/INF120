# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 08:18:34 2020

@author: Tor Erik
"""
import math

def pytagoras(katet1,katet2):
    hyp=math.sqrt(katet1**2+katet2**2)
    return hyp

x=3
y=4
hypotenus = pytagoras(3,4)
print("En trekant med lengdene:", x, y)
print("Gir en hypotenus med lengden",hypotenus)


def finn_avstand_til_origo(x,y):
    return pytagoras(x,y)

x=4
y=3
avstand_til_origo = finn_avstand_til_origo(x,y)


from turtle import *

def tegn_mangekansblomst(antall_blad, antall_sider_per_blad, omkrets):
    vinkel=360/antall_blad
    for side in range(antall_blad):
        tegn_mangekant(antall_sider_per_blad, omkrets)
        right(vinkel)
        
def tegn_mangekant(antall_sider, omkrets):
    vinkel=360/antall_sider
    sidelengde=omkrets/antall_sider
    for side in range(antall_sider):
        forward(sidelengde)
        right(vinkel)



def tegn_rotert_mangekant(omkrets):
    right(30)
    tegn_mangekant(6,omkrets)
    left(30)
    
def tegn_sekskantrad(omkrets,antall_sekskanter):
    for rad in range(antall_sekskanter):
        tegn_rotert_mangekant(omkrets)
        penup(),forward(40),pendown()
        
    penup(), backward(40*antall_sekskanter), pendown()
    
    
def tegn_sekskantpar(omkrets, antall_sekskanter):
    tegn_sekskantrad(omkrets, antall_sekskanter)
    penup(),right(90), forward(40),left(90), forward(20),pendown()
    tegn_sekskantrad(omkrets, antall_sekskanter),
    penup(),forward(-20),
    right(90)
    forward(40)
    left(90)
    pendown()

for radpar in range(3):
    tegn_sekskantpar(200,5)
    
speed(5)    
