# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:38:32 2026

@author: 24daai01
"""

from Dicegroup import DiceGroup
import Score_calculator

if __name__ == "__main__":
    info = "Tryck 'Enter' för att kasta tärningarna. Välja vilka tärningar du vill behålla (1-5). Om du vill avsluta skriv 'q': "
    dg = DiceGroup()
    cap = 0
    while cap < 3:
        choice = input(info)

        if choice.lower() == 'q':
            break

        if choice != "":
            choice_clean = choice.replace(" ", "")
            for ch in choice:
                if ch.isdigit():
                    dg.hold(int(ch)-1)
            print(dg)

        if choice == "":
            dg.roll()
            print(dg)
            info = "Välj vilka tärningar du vill behålla: "
            cap += 1


values = dg.values()
h = Score_calculator.histogram(values)

print("\nPoäng:")
for category, func in Score_calculator.fd.items():
    print(f"{category}: {func(h)}")
