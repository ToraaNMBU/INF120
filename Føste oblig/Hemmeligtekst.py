# -*- coding: utf-8 -*-
"""
_author_ Tor Erik Aasestad
_email_ toraa@nmbu.no

"""
from turtle import *
import time
speed(3)
pensize(2)

setup( width = 1500, height = 400, startx = None, starty = None)





def tegn_a():
    left(80)
    forward(100)
    left(200)
    forward(60)
    left(80)
    forward(-22)
    forward(22)
    right(80)
    forward(40)
    

#tegn_a()
#time.sleep(5)
clear()
penup(),home(),pendown()


def tegn_b():
    left(90)
    forward(90)
    right(90)
    for x in range(25):
        forward(3)
        right(8)
    forward(-10)
    right(180)
    for x in range(22):
        forward(3)
        right(8)
    sety(0)
    setheading(0)

def tegn_c():
    left(180)
    forward(15)
    for x in range(60):
        forward(2)
        right(3)
    forward(15)

def tegn_d():
    left(90)
    forward(90)
    right(90)
    for x in range(180):
        forward(0.75)
        right(1)

def tegn_e():
    left(90)
    forward(90)
    right(90)
    forward(35)
    forward(-35)
    left(90)
    forward(-45)
    right(90)
    forward(35)
    forward(-35)
    left(90)
    forward(-45)
    right(90)
    forward(35)

def tegn_f():
    left(90)
    forward(90)
    right(90)
    forward(35)
    forward(-35)
    left(90)
    forward(-45)
    right(90)
    forward(35)
    forward(-35)
    left(90)
    forward(-45)
    setheading(0)


def tegn_g():
    forward(40)
    left(90)
    forward(35)
    left(90)
    forward(20)
    forward(-20)
    right(90)
    forward(-35)
    right(90)
    forward(-70)
    left(90)
    forward(90)
    right(90)
    forward(70)
    right(90)
    forward(40)

def tegn_h():
    left(90)
    forward(80)
    forward(-40)
    right(90)
    forward(45)
    left(90)
    forward(40)
    forward(-80)
    
def tegn_i():
    left(90)
    forward(80)
    forward(-80)

def tegn_j():
    color('white')
    sety(25)
    color('black')
    right(270)
    for x in range(90):
        forward(-0.75)
        left(2)
    forward(-55)
    
    
def tegn_k():
    left(90)
    forward(80)
    forward(-40)
    right(35)
    forward(50)
    forward(-50)
    right(100)
    forward(50)
        
def tegn_l():
    left(90)
    forward(80)
    forward(-80)
    right(90)
    forward(50)

def tegn_m():
    left(90)
    forward(80)
    right(150)
    forward(50)
    left(120)
    forward(50)
    setheading(0)
    right(90)
    forward(80)

def tegn_n():
    left(90)
    forward(80)
    right(150)
    forward(90)
    setheading(0)
    left(90)
    forward(80)

def tegn_o():
    for x in range(120):
        forward(3)
        left(4.2)
def tegn_p():
    left(90)
    forward(80)
    right(90)
    for x in range(20):
        forward(4)
        right(10)

def tegn_q():
    for x in range(95):
        forward(3)
        left(4.2)
    left(90)
    forward(30)
    forward(-40)

def tegn_r():
    tegn_p()
    setheading(0)
    right(50)
    forward(45)


def tegn_t():
    left(90)
    forward(80)
    left(90)
    forward(40)
    forward(-80)
    
def tegn_u():
    left(90)
    penup(),forward(80), pendown()
    right(180)
    forward(30)
    for halvsirkel in range (45):
        forward(3)
        left(4)
    forward(30)

    
def mellom_bokstaver():
    penup()
    setheading(0)
    sety(0)
    forward(100)    
    pendown()
def mellom_ord():
    mellom_bokstaver()
    mellom_bokstaver()
    
    

def hei_på_deg():
    reset()
    reset(), penup(), setx(-600),pendown()
    tegn_h()
    mellom_bokstaver()
    tegn_e()
    mellom_bokstaver()
    tegn_i()
    mellom_ord()
    tegn_p()
    mellom_bokstaver()
    tegn_a()
    mellom_bokstaver()
    tegn_a()
    mellom_bokstaver()
    mellom_bokstaver()
    tegn_d()
    mellom_bokstaver()
    tegn_e()
    mellom_bokstaver()
    tegn_g()
    time.sleep(5)

def flex_av_fritid():
    reset()
    tegn_a()
    mellom_bokstaver()
    tegn_b()
    mellom_bokstaver()
    mellom_bokstaver()
    tegn_c()
    mellom_bokstaver()
    tegn_d()
    mellom_bokstaver()
    tegn_e()
    time.sleep(10)
    reset(), penup(), setx(-600),pendown()
    tegn_f()
    mellom_bokstaver()
    tegn_g()
    mellom_bokstaver()
    tegn_h()
    mellom_bokstaver()
    tegn_i()
    mellom_bokstaver()
    tegn_j()
    mellom_bokstaver()
    tegn_k()
    time.sleep(10)
    reset(), penup(), setx(-600),pendown()
    tegn_l()
    mellom_bokstaver()
    tegn_m()
    mellom_bokstaver()
    tegn_n()
    mellom_bokstaver()
    tegn_o()
    mellom_bokstaver()
    tegn_p()
    mellom_bokstaver()
    tegn_q()

def fin_dag():
    reset(), penup(),setx(-600),pendown()
    tegn_h()
    mellom_bokstaver()
    tegn_a()
    mellom_bokstaver()
    tegn_a()
    mellom_bokstaver()
    tegn_p()
    mellom_bokstaver()
    tegn_e()
    mellom_bokstaver()
    tegn_r()
    mellom_ord()
    tegn_d()
    mellom_bokstaver()
    tegn_u()
    time.sleep(4)
    reset(), penup(), setx(-600),pendown()
    mellom_ord()
    tegn_h()
    mellom_bokstaver()
    tegn_a ()
    mellom_bokstaver()
    tegn_r()
    mellom_ord()
    tegn_e()
    mellom_bokstaver()
    tegn_n()
    time.sleep(4)
    reset(), penup(), setx(-600),pendown()
    tegn_f()
    mellom_bokstaver()
    tegn_i()
    mellom_bokstaver()
    tegn_n()
    mellom_ord()
    tegn_d()
    mellom_bokstaver()
    tegn_a()
    mellom_bokstaver()
    tegn_g()
    time.sleep(5)

def keep_going():
    reset(), penup(), setx(-600),pendown()
    tegn_k()
    mellom_bokstaver()
    tegn_e()
    mellom_bokstaver()
    tegn_e()
    mellom_bokstaver()
    tegn_p()
    mellom_ord()
    tegn_g()
    mellom_bokstaver()
    tegn_o()
    mellom_bokstaver()
    tegn_i()
    mellom_bokstaver()
    tegn_n()
    mellom_bokstaver()
    tegn_g()
    
hei_på_deg()
fin_dag()

flex_av_fritid()
keep_going()
done()