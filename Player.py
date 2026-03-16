# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:40:07 2026

@author: 24daai01
"""

def player_maker():
    # Fråga antal spelare
    while True:
        try:
            antal = int(input("Hur många spelare ska spela? "))
            if antal > 0:
                break
            else:
                print("Antal spelare måste vara minst 1.")
        except ValueError:
            print("Skriv ett heltal för antal spelare.")


    player_list = []
    for i in range(antal):
        namn = input(f"Skriv namn på spelare {i+1}: ")
        player_list.append({"namn": namn})

    return player_list
