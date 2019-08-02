# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:39:30 2019

@author: akshay_gane
"""

import os

def rename_files():
    file_list = os.listdir(r"D:\TeXT_CA\Python\prank\prank")
    saved_path=os.getcwd()
    print("Current Working Directory Is " +saved_path)
    os.chdir(r"D:\TeXT_CA\Python\prank\prank")
    
    for file_names in file_list:
        os.rename(file_names, file_names.translate({ ord(c): '' for c in "0123456789"}))
    #print(file_list)
rename_files()