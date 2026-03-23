# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:39:13 2026

@author: 24daai01
"""
#importerar random modulen så att vi kan ha slumpmässigt val då python egentligen inte har dedt inbyggt
import random
#här gör vi våran tärning
class Dice:
    
    def __init__(self):
        self.__eyes = 0      
        self.unhold()            
        self.roll()            
        
    def roll(self):
        if not self.is_held():
            self.__eyes = random.randint(1, 6)   
        self.unhold()             
        
    def get_eyes(self):
        return self.__eyes   
    
    def is_held(self):
        return self.__held   
    
    def hold(self):
        self.__held = True
    
    def unhold(self):
        self.__held = False           
    
    def __str__(self):      
        if self.is_held():
            return f"[{self.__eyes:d}]"
        else:
            return f"<{self.__eyes:d}>"
        
    def __repr__(self):     
        return f"Die({self.__eyes:d})"
    
    eyes = property(get_eyes)
