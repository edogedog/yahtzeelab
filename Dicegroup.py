# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:35:40 2026

@author: 24daai01
"""

from Dice import Dice

class DiceGroup:

    def __init__(self, N=5):
        self.__Dice_list = [Dice() for _ in range(N)]
   
    def roll(self):
        for d in self.__Dice_list:
            d.roll()
    
    def get_die(self, n):
        return self.__Dice_list[n%len(self.__Dice_list)]
    
   
    def hold(self, n):
        self.get_die(n).hold()
    
   
    def unhold(self, n):
        self.get_die(n).unhold()


    def values(self):
        return[d.eyes for d in self.__Dice_list]   


    def __str__(self):
        return " ".join(map(str,self.__Dice_list))
