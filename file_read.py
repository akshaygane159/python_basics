# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:59:09 2019

@author: akshay_gane
"""
import urllib.request
def read_file():
    file_open = open("D:\TeXT_CA\Python\movie_quotes.txt")
    file_content = file_open.read()
    print(file_content)
    file_open.close()
    profanity_checking(file_content)

def profanity_checking(validate_content):
    with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+validate_content) as connect:
        result = connect.read()
        print(result)
        connect.close()
    
read_file()