# -*- coding: utf-8 -*-

def make_empty_scoreboard(fd):
    return {key: None for key in fd.keys()}


def create_playerboards(player_list, fd):
    playerboards = {}

    for play in player_list:
        playerid = play["id"]
        playerboards[playerid] = make_empty_scoreboard(fd)

    return playerboards


def upper_section_total(playerboard):
    keys = ["Ettor", "Tvåor", "Treor", "Fyror", "Femmor", "Sexor"]
    total = 0

    for key in keys:
        value = playerboard[key]
        if value is not None:
            total += value

    return total


def bonus_score(playerboard):
    if upper_section_total(playerboard) >= 63:
        return 50
    return 0


def total_score(playerboard):
    total = 0

    for value in playerboard.values():
        if value is not None:
            total += value

    total += bonus_score(playerboard)
    return total


def print_scoreboard(playerboard, namn=""):
    if namn != "":
        print(f"\nScoreboard för {namn}:")
    else:
        print("\nScoreboard:")

    for key, value in playerboard.items():
        if value is None:
            print(f"{key}: Ej vald")
        else:
            print(f"{key}: {value}")

    print(f"Bonus: {bonus_score(playerboard)}")
    print(f"Total poäng: {total_score(playerboard)}")
