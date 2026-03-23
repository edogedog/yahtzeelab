# -*- coding: utf-8 -*-


#Skapar histogram för att se värdet på varje träning som kastas och sparar det i en list
def make_histogram(dice):
    h = [0, 0, 0, 0, 0, 0]
    for die in dice:
        h[die - 1] += 1
    return h

#Enkal funktioner, kollar på index 0, det ettor representerar
#Muliplicerar det med 1
def score_ones(h):
    return h[0] * 1

#Samma här men checkar index 1 och muliplicerar med 2
def score_twos(h):
    return h[1] * 2

#Index 2 * 3
def score_threes(h):
    return h[2] * 3

#Index 3 * 4
def score_fours(h):
    return h[3] * 4

#Index 4 * 5
def score_fives(h):
    return h[4] * 5

#Index 5 * 6
def score_sixes(h):
    return h[5] * 6

#Lite mer avancerad poängsystem. börjar på index 5 och går baklängs
#Detta görs för att hitta bästa möjliga poängmässiga paret
def score_pair(h):
    for i in range(5, -1, -1):
        if h[i] >= 2:
            return (i + 1) * 2
    return 0


def score_two_pair(h):
    pairs = []
    for i in range(5, -1, -1):
        if h[i] >= 2:
            pairs.append(2 * (i + 1))
    if len(pairs) >= 2:
        return pairs[0] + pairs[1]
    return 0


def score_three_of_a_kind(h):
    for i in range(5, -1, -1):
        if h[i] >= 3:
            return 3 * (i + 1)
    return 0


def score_four_of_a_kind(h):
    for i in range(5, -1, -1):
        if h[i] >= 4:
            return 4 * (i + 1)
    return 0

#Kollar med slice operatorn om index 0-4 har ett värde
#Samt kollar vi om index 5 är 0
def score_low_straight(h):
    if h[0:5] == [1, 1, 1, 1, 1] and h[5] == 0:
        return 15
    return 0


def score_high_straight(h):
    if h[1:6] == [1, 1, 1, 1, 1] and h[0] == 0:
        return 20
    return 0


def score_full_house(h):
    if 3 in h and 2 in h:
        i = h.index(3)
        j = h.index(2)
        return 3 * (i + 1) + 2 * (j + 1)
    return 0


def score_chance(h):
    total = 0
    for i in range(len(h)):
        total += h[i] * (i + 1)
    return total

#Enkel koll om alla träningar är samma värde
def score_yatzy(h):
    if 5 in h:
        return 50
    return 0


#Nycklarna är namn på alla funktioner och värderna är hur funktionerna räknar poöngen
fd = {
    "Ettor": score_ones,
    "Tvåor": score_twos,
    "Treor": score_threes,
    "Fyror": score_fours,
    "Femmor": score_fives,
    "Sexor": score_sixes,
    "Ett par": score_pair,
    "Två par": score_two_pair,
    "Tretal": score_three_of_a_kind,
    "Fyrtal": score_four_of_a_kind,
    "Liten stege": score_low_straight,
    "Stor stege": score_high_straight,
    "Kåk": score_full_house,
    "Chans": score_chance,
    "Yatzy": score_yatzy
}


#Vi använder oss av histogram funktionen
#Loopar genom alla kateogirer i fd. Om ej vald förblir kategorin none
#De lediga kategorierna checkas beräknas med fd[key](h)
#Loopar genom varje ledig kategri och använder sig av funktionerna för att visa poängen
def get_available_scores(values, playerid, playerboards):
    h = make_histogram(values)
    tally = {}

    for key in fd:
        if playerboards[playerid][key] is None:
            tally[key] = fd[key](h)
#Retunerar en nya dictionary med kategorinamn + poäng
    return tally

#Använder oss av funktionen över så vi kan göra "scoreborden" interaktiv för mänskliga spelare
def choose_score_human(values, playerid, playerboards):
    tally = get_available_scores(values, playerid, playerboards)
    
#Vissar spelaren vad som finns att väljas
    print("\nValbara kategorier:")
    for key, value in tally.items():
        print(f"{key}: {value}")

    while True:
        choice = input("Vilken kategori vill du välja? ").strip()

#Gör det case - sensitive så att spelaren kan skriva "ett par", "ETT PAR" och "EtT PaR"
#Vi gör även key till små bokstäver så det matchar vad användaren skrev
        for key in tally:
            if key.lower() == choice.lower():
                playerboards[playerid][key] = tally[key]
                print(f"Du valde {key} och fick {tally[key]} poäng.")
                return tally[key]

        print("Ogiltigt val, skriv namnet på en kategori.")


#Hämtar återigen funktionen som är ligger lite över
#Boten är enkel och väljer bara det värde på träningar som ger mest poäng
#boten kan varken hålla eller tänka vad som är bäst eller strycka under någon kategori. Simpel och rakt på sak
def choose_score_bot(values, playerid, playerboards, namn):
    tally = get_available_scores(values, playerid, playerboards)

    best_key = None
    best_value = -1

#Checkar det bästa värdet efter alla tre kasen boten gör
#Lägger  det bästa värdet i best_value (poängen) och best_key får själva kategorinamnet 
    for key, value in tally.items():
        if value > best_value:
            best_value = value
            best_key = key

    playerboards[playerid][best_key] = best_value
    print(f"{namn} valde {best_key} och fick {best_value} poäng.")
    return best_value
