# -*- coding: utf-8 -*-

def make_histogram(dice):
    h = [0, 0, 0, 0, 0, 0]
    for die in dice:
        h[die - 1] += 1
    return h


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


def score_yatzy(h):
    if 5 in h:
        return 50
    return 0


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


def get_available_scores(values, playerid, playerboards):
    h = make_histogram(values)
    tally = {}

    for key in fd:
        if playerboards[playerid][key] is None:
            tally[key] = fd[key](h)

    return tally


def choose_score_human(values, playerid, playerboards):
    tally = get_available_scores(values, playerid, playerboards)

    print("\nValbara kategorier:")
    for key, value in tally.items():
        print(f"{key}: {value}")

    while True:
        choice = input("Vilken kategori vill du välja? ").strip()

        choice_lower = choice.lower()

        for key in tally:
            if key.lower() == choice_lower:
                playerboards[playerid][key] = tally[key]
                print(f"Du valde {key} och fick {tally[key]} poäng.")
                return tally[key]

        print("Ogiltigt val, skriv namnet på en kategori.")


def choose_score_bot(values, playerid, playerboards, namn):
    tally = get_available_scores(values, playerid, playerboards)

    best_key = None
    best_value = -1

    for key, value in tally.items():
        if value > best_value:
            best_value = value
            best_key = key

    playerboards[playerid][best_key] = best_value
    print(f"{namn} valde {best_key} och fick {best_value} poäng.")
    return best_value
