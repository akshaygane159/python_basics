# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:21:13 2019

@author: akshay_gane
"""

import turtle
    
def draw_triangle():
        canvas = turtle.Screen()
        canvas.bgcolor("red")
        turtle_obj2 = turtle.Turtle()
        turtle_obj2.color("yellow")
        turtle_obj2.forward(100)
        turtle_obj2.left(120)
        turtle_obj2.forward(100)
        turtle_obj2.left(120)
        turtle_obj2.forward(100)
        canvas.exitonclick()

draw_triangle()