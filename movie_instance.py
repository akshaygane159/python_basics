# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:23:36 2019

@author: akshay_gane
"""

import movie_blueprint

toy_story = movie_blueprint.Movies("Toy Story",
                       "stroy of boy and his toys",
                       "https://www.imdb.com/title/tt0114709/",
                       "https://www.youtube.com/watch?reload=9&v=wmiIUN-7qhE")

i = input("what do you want to know about movie: 1. title 2. storyline 3. poster 4. trailer")

if int(i) == 1 :
    print(toy_story.title)
if int(i) == 2 :
    print(toy_story.storyline)
if int(i) == 3 :
    toy_story.show_poster()
if int(i) == 4 :
    toy_story.show_trailer()
    
#print(toy_story.title)
#toy_story.show_trailer()
#toy_story.show_poster()
