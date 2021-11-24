from turtle import *

def ruutude_fraktal(sügavus, pikkus):
    

    for i in range(3):
        forward(pikkus)

        if sügavus > 1:
            pikkus /= 2
            ruutude_fraktal(sügavus - 1,pikkus)
            pikkus *= 2

        right(90)

    forward(pikkus)
    right(90)

ruutude_fraktal(4, 100)

exitonclick()
        
        
    