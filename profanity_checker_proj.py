# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:16:51 2019

@author: akshay_gane
"""
from profanity import profanity

def read_file():
    file_open = open("D:\TeXT_CA\Python\movie_quotes.txt")
    file_content = file_open.read()
    print(file_content)
    print("-----------------------------")
    file_open.close()
    profanity_checking(file_content)

def profanity_checking(validate_content):
   result = profanity.contains_profanity(validate_content)
   print(result)
   if result == True:
      print("Profanity alert!!!")
   if result == False:
      print("No Profanity :)")
   print(profanity.censor(validate_content))

read_file()