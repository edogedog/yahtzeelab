# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:39:22 2026

@author: 24daai01
"""

dielist = [3,3,4,3,2]

dictlist = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}


for i in dielist:
    if i in dictlist:
        dictlist[i] += 1

h = list(dictlist.values())

print(h)

def three_of_a_kind(h):
