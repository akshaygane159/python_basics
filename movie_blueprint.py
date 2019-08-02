# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:06:12 2019

@author: akshay_gane
"""
import webbrowser

class Movies():
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    def show_poster(self):
        webbrowser.open(self.poster_image_url)
    