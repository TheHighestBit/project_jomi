from turtle import *

def fraktal(tase, pikkus):
    if tase >= 1:
        forward(pikkus)
        fraktal(tase-1,0.7*pikkus)
        left(120)
        forward(pikkus)
        left(120)
        forward(pikkus)
        left(120)

fraktal(8,100)
exitonclick()