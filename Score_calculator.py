# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:39:22 2026

@author: 24daai01
"""

dielist = [5, 1, 4, 5, 3]

dictlist = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}


for i in dielist:
    if i in dictlist:
        dictlist[i] += 1

h = list(dictlist.values())

print(h)


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



def score_pair(h):
    result = 0
    if 2 in h:
        result =  2 * (1 + h.index(3)) # 3 * det tärningsvärde som hittades tre av
    return result

print("Poäng för 1 par: ", score_pair(h))
    

def score_two_pair(h):
   result = 0
   if 2 in h and 2 in h:
       i = h.index(2)
       j = h.index(2)
       result = 2 * (i+1) + 2 (j+1)
   return result
    

def score_three_of_a_kind(h):
    result = 0
    if 3 in h:
        result =  3 * (1 + h.index(3)) # 3 * det tärningsvärde som hittades tre av
    return result
    

def score_four_of_a_kind(h):
    result = 0
    if 4 in h:
        result =  4 * (1 + h.index(3)) # 3 * det tärningsvärde som hittades tre av
    return result

def score_low_straight(h):
    if h[0:5].count(1) == 5 and h[5] == 0:
        return 15
    return 0


def score_high_straight(h):
    if h[1:6].count(1) == 5 and h[0] == 0:
        return 20
    return 0



def score_full_house(h):
    result = 0
    if 3 in h and 2 in h:
        i = h.index(3)
        j = h.index(2)
        result = 3 * (i+1) + 2 (j+1)
    return result




def score_chance(h):
    result = 0
    for i in range(len(h)):
        result += h[i] (i + 1)
    return result



def score_yatzy(h):
    if 5 in h:
        return 50
    return 0



"""
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
"""
