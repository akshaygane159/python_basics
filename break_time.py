# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:55:38 2019

@author: akshay_gane
"""

import webbrowser
import time

#4 breaks per two hours
breakTime = 0
while(breakTime <= 3):
    time.sleep(7200)
    webbrowser.open("https://www.google.com/")
    breakTime+=1