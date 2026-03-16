# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:38:32 2026

@author: 24daai01
"""

from Dicegroup import DiceGroup
import Score_calculator
from Player import player_maker

if __name__ == "__main__":
    player_list = player_maker()  
    


    for play in player_list:
        playor = int(len(play))-1
        playerid = str(playor)  
        argument1 = playerid
        print(f"\nDet är {play['namn']}s tur!")
        dg = DiceGroup()
        cap = 0
        info = "Tryck 'Enter' för att kasta tärningarna: "

        while cap < 3:
            choice = input(info)

            if choice.lower() == 'q':
                break

            if choice != "":
                choice_clean = choice.replace(" ", "")
                for ch in choice_clean:
                    if ch.isdigit():
                        dg.hold(int(ch)-1)
                print("Efter att ha hållit tärningarna:", dg)

            dg.roll()
            print("Efter kast:", dg)

            cap += 1
            info = "Välj vilka tärningar du vill behålla (1-5) eller tryck Enter för att kasta igen: "
            
values = dg.values()
h = Score_calculator.histogram(values)
poang = Score_calculator.score(h)
