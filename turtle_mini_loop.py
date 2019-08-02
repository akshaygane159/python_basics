# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:31:51 2019

@author: akshay_gane
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:48:10 2019

@author: akshay_gane
"""

import turtle

def draw_traingle():
    canvas = turtle.Screen()
    canvas.bgcolor("black")
    turtle_obj = turtle.Turtle()
    turtle_obj.color("yellow")
    turtle_obj.shape("turtle")
    turtle_obj.speed(2)
    count = 0
    while count < 3:
        turtle_obj.forward(100)
        turtle_obj.left(120)
        count += 1
    #icount = 0
    #while icount < 3:
    turtle_obj.forward(50)
    turtle_obj.left(60)
    turtle_obj.forward(50)
    icount = 0
    while icount < 2:
        turtle_obj.left(120)
        turtle_obj.forward(50)
        icount += 1
    canvas.exitonclick()
    
draw_traingle()