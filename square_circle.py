# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:16:25 2019

@author: akshay_gane
"""

import turtle

def draw_square(other_obj):
    for i in range(1, 5):
        other_obj.forward(100)
        other_obj.right(90)
    
def draw_circle_using_square():
    canvas = turtle.Screen()
    canvas.bgcolor("black")
    turtle_obj = turtle.Turtle()
    turtle_obj.color("yellow")
    turtle_obj.shape("turtle")
    turtle_obj.speed(2)
    for i in range(1, 40):
        draw_square(turtle_obj)
        turtle_obj.left(10)
    canvas.exitonclick()

draw_circle_using_square()