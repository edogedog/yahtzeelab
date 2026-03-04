# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:38:32 2026

@author: 24daai01
"""

from Dicegroup import DiceGroup

if __name__ == "__main__":
    info = "Tryck 'Enter' för att kasta tärningarna. Välja vilka träningar du vill behålla 1 - 5. Om du vill avsluta skriv 'q': "
    dg = DiceGroup()
    cap = 2
    while cap < 3:
        choice = input(info)
        if choice != "":
            for ch in choice:
                dg.hold(int(ch)-1)
                print(dg)
        if choice == "":
            dg.roll()
            print(dg)
            info = "Välj vilka träningar du vill behålla: "
            cap += 1
        elif choice.lower() == 'q':

            break
