# -*- coding: utf-8 -*-

def make_empty_scoreboard(fd):
    return {key: None for key in fd.keys()}


def create_playerboards(player_list, fd):
    playerboards = {}

    for play in player_list:
        playerid = play["id"]
        playerboards[playerid] = make_empty_scoreboard(fd)

    return playerboards


def print_scoreboard(playerboard, namn=""):
    if namn != "":
        print(f"\nScoreboard för {namn}:")
    else:
        print("\nScoreboard:")

    for key, value in playerboard.items():
        print(f"{key}: {value}")
