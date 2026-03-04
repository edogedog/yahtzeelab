# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:39:22 2026

@author: 24daai01
"""

dielist = [1,2,3,4,5,6]

dictlist = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}


for i in dielist:
    if i in dictlist:
        dictlist[i] += 1

h = list(dictlist.values())

print(h)

#här är en massa fina funktioner av acailable scores vi ska checka om h är, vi ska definera dessa så de checkar för hn, etta pax ja tar three of kind four of kinf o kåååk
def score_ones(h):
    return h[0] * 1

def score_twos(h):
    return h[1] * 2

def score_threes(h):
    return h[2] * 3

def score_fours(h):
    return h[3] * 4

def score_fives(h):
    return h[4] * 5

def score_sixes(h):
    return h[5] * 6

print("Poäng för Ettor:", score_ones(h))  # Förväntad output: 0
print("Poäng för Tvåor:", score_twos(h))  # Förväntad output: 2 (1 tvåa * 2)
print("Poäng för Treor:", score_threes(h))  # Förväntad output: 9 (3 treor * 3)
print("Poäng för Fyror:", score_fours(h))  # Förväntad output: 4 (1 fyra * 4)
print("Poäng för Femmor:", score_fives(h))  # Förväntad output: 0
print("Poäng för Sexor:", score_sixes(h))  # Förväntad output: 0



def score_pair(h):

def score_two_pair(h):

def score_three_of_a_kind(h):

def score_four_of_a_kind(h):

def score_low_straight(h):

def score_high_straight(h):
    

def score_full_house(h):
    i = h.index(3)
    j = h.index(2)
    if i>=0 and j>=0:
        result = 3 * (i+1) + 2 *(j+1)
        return result
    
# Histogrammet för tärningskast: [6, 6, 6, 3, 3]
histogram = [0, 0, 1, 2, 0, 3]  # 3 stycken 6:or, 2 stycken 3:or
print(score_full_house(histogram))  # Förväntad output: 3 * 6 + 2 * 3 = 18 + 6 = 24


def score_chance(h):

def score_yatzy(h):
    
#här gör vi en dictionary grejsimojs som vi sedan kommer gå igenom där vi checkar igenom alla våra funtkioner med en for loop där de kommer va tyyyyp fonånting, nånting in fd: o sen under de typ cat för categori o fun för funktion
fd = {
    "Ettor": score_ones,
    "Tvåor": score_twos,
    "Treor": score_threes,
    "Fyror": score_fours,
    "Femmor": score_fives,
    "Sexor": score_sixes,
    "1 par": score_pair,
    "2 par": score_two_pair,
    "Tretal": score_three_of_a_kind,
    "Fyrtal": score_four_of_a_kind,
    "Liten stege": score_low_straight,
    "Stor stege": score_high_straight,
    "Kåk": score_full_house,
    "Chans": score_chance,
    "Yatzy": score_yatzy
}
