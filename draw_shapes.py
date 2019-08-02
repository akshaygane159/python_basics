# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:01:27 2019

@author: akshay_gane
"""

import turtle
    
def draw_square():
        canvas = turtle.Screen()
        canvas.bgcolor("red")
        turtle_obj = turtle.Turtle()
        turtle_obj.color("white")
        count = 0
        while count<=3:
            turtle_obj.forward(50)
            turtle_obj.right(90)
            count += 1
                    
        canvas.exitonclick()

def draw_circle():
        canvas1 = turtle.Screen()
        canvas1.bgcolor("red")        
        turtle_obj1 = turtle.Turtle()
        turtle_obj1.color("yellow")
        turtle_obj1.circle(radius = 70)
        canvas1.exitonclick()

def draw_triangle():
        canvas2 = turtle.Screen()
        canvas2.bgcolor("red")
        turtle_obj2 = turtle.Turtle()
        turtle_obj2.color("yellow")
        turtle_obj2.forward(100)
        turtle_obj2.left(120)
        turtle_obj2.forward(100)
        turtle_obj2.left(120)
        turtle_obj2.forward(100)
        canvas2.exitonclick()
        
i = input("Enter your choice 1. Draw square 2. Draw circle 3. Draw triangle")
if int(i) == 1 :
    draw_square()
if int(i) == 2 :
    draw_circle()
if int(i) == 3 :
    draw_triangle()
  
