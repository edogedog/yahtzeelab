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

#här är en massa fina funktioner av acailable scores vi ska checka om h är, vi ska definera dessa så de checkar för hn, etta pax ja tar three of kind four of kinf o kåååk
def score_ones(h):

def score_twos(h):

def score_threes(h):

def score_fours(h):

def score_fives(h):

def score_sixes(h):

def score_pair(h):

def score_two_pair(h):

def score_three_of_a_kind(h):

def score_four_of_a_kind(h):

def score_low_straight(h):

def score_high_straight(h):

def score_full_house(h):

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
