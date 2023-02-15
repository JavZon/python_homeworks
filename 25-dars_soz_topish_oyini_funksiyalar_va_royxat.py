# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:40:16 2023

@author: kodir
"""

# https://github.com/JavZon/python-darslar/blob/main/26-projects-soz-topish/soz-topish/uzwords.py


from uzwords import words
from random import choice

def display():
     tasodifiy_soz=choice(words)
     return tasodifiy_soz.upper()
 



def namoyish_et(harflar, soz):
    jami_harflar=""
    
    for a in soz:
        if a in harflar:
            jami_harflar+=a
        else:
            jami_harflar+="-"
    return jami_harflar            

lll=display()

x=''        
print(namoyish_et(x,lll))
print(lll)           




















