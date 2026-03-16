# -*- coding: utf-8 -*-

from Dicegroup import DiceGroup
import Score_calculator
import Scoreboard
from Player import player_maker


def all_scoreboards_filled(playerboards):
    for board in playerboards.values():
        if None in board.values():
            return False
    return True


if __name__ == "__main__":
    player_list = player_maker()
            # skriv ut välkomstmeddelande
    names = [p["namn"] for p in player_list]
    
    if len(names) == 1:
        welcome = names[0]
    elif len(names) == 2:
        welcome = f"{names[0]} och {names[1]}"
    else:
        welcome = ", ".join(names[:-1]) + " och " + names[-1]
    print("\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n")

    print(f"\nVälkomna {welcome}!\n")

    print("\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ \n ")
    
    playerboards = Scoreboard.create_playerboards(player_list, Score_calculator.fd)

    while not all_scoreboards_filled(playerboards):
        for play in player_list:
            playerid = play["id"]

            if None not in playerboards[playerid].values():
                continue

            print(f"\nDet är {play['namn']}s tur!")

            dg = DiceGroup()
            cap = 0
            info = "Tryck Enter för att kasta tärningarna: "

            while cap < 3:
                if play["bot"]:
                    dg.roll()
                    cap += 1
                    print("Efter kast:", dg)
                    continue

                choice = input(info)

                if choice.lower() == "q":
                    break

                if choice != "":
                    choice_clean = choice.replace(" ", "")
                    for ch in choice_clean:
                        if ch.isdigit():
                            n = int(ch) - 1
                            if 0 <= n <= 4:
                                dg.hold(n)
                    print("Efter att ha hållit tärningarna:", dg)

                dg.roll()
                print("Efter kast:", dg)

                cap += 1
                info = "Välj vilka tärningar du vill behålla (1-5) eller tryck Enter för att kasta igen: "

            values = dg.values()

            if play["bot"]:
                gained_points = Score_calculator.choose_score_bot(
                    values, playerid, playerboards, play["namn"]
                )
            else:
                gained_points = Score_calculator.choose_score_human(
                    values, playerid, playerboards
                )

            play["poang"] += gained_points

            print(f"{play['namn']} har nu totalt {play['poang']} poäng.")
            Scoreboard.print_scoreboard(playerboards[playerid], play["namn"])
    print("\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ \n ")
    print("\nSLUTRESULTAT:")
    print("\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ \n ")
    ranking = sorted(player_list, key=lambda p: p["poang"], reverse=True)

    for i, play in enumerate(ranking, start=1):
        print(f"{i}. {play['namn']} - {play['poang']} poäng")

    print(f"\nVinnare: {ranking[0]['namn']} med {ranking[0]['poang']} poäng")
    print(f"Förlorare: {ranking[-1]['namn']} med {ranking[-1]['poang']} poäng")
