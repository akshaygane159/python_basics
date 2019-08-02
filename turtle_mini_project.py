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
    turtle_obj.forward(100)
    turtle_obj.left(120)
    turtle_obj.forward(100)
    turtle_obj.left(120)
    turtle_obj.forward(100)
    turtle_obj.left(120)
    turtle_obj.forward(50)
    turtle_obj.left(120)
    turtle_obj.forward(50)
    turtle_obj.right(120)
    turtle_obj.forward(50)
    turtle_obj.right(120)
    turtle_obj.forward(50)
    turtle_obj.left(120)
    turtle_obj.forward(25)
    turtle_obj.left(120)
    turtle_obj.forward(25)
    turtle_obj.right(120)
    turtle_obj.forward(25)
    turtle_obj.right(120)
    turtle_obj.forward(25)
    turtle_obj.right(60)
    turtle_obj.forward(50)
    turtle_obj.right(60)
    turtle_obj.forward(25)
    turtle_obj.right(120)
    turtle_obj.forward(25)
    turtle_obj.right(120)
    turtle_obj.forward(25)
    turtle_obj.right(60)
    turtle_obj.forward(25)
    turtle_obj.right(120)
    turtle_obj.forward(75)
    turtle_obj.right(60)
    turtle_obj.forward(25)
    turtle_obj.right(120)
    turtle_obj.forward(25)
    turtle_obj.right(120)
    turtle_obj.forward(25)
    canvas.exitonclick()
    
draw_traingle()