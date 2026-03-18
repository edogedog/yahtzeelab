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

    names = [p["namn"] for p in player_list]

    if len(names) == 1:
        welcome = names[0]
    elif len(names) == 2:
        welcome = f"{names[0]} och {names[1]}"
    else:
        welcome = ", ".join(names[:-1]) + " och " + names[-1]

    print("\n----------------------------------")
    print(f"Välkommen {welcome}!")
    print("----------------------------------\n")

    playerboards = Scoreboard.create_playerboards(player_list, Score_calculator.fd)

    while not all_scoreboards_filled(playerboards):
        for play in player_list:
            playerid = play["id"]

            if None not in playerboards[playerid].values():
                continue

            print("\n----------------------------------")
            print(f"Det är {play['namn']}s tur!")
            print("----------------------------------\n")

            dg = DiceGroup()

            dg.roll()
            cap = 1
            print("Första kastet är:", dg)

            info = "Välj vilka tärningar du vill behålla (1-5) eller tryck 'Enter' för att kasta igen: "

            while cap < 3:
                if play["bot"]:
                    dg.roll()
                    cap += 1
                    print(f"Robotkast {cap}: {dg}")
                    continue

                choice = input(info)

                if choice.lower() == "q":
                    print(f"{play['namn']} gav upp rundan.")
                    break

                if choice != "":
                    choice_clean = choice.replace(" ", "")
                    for ch in choice_clean:
                        if ch.isdigit():
                            n = int(ch) - 1
                            if 0 <= n <= 4:
                                dg.hold(n)
                    print("Tärningarna du håller: ", dg)

                dg.roll()
                cap += 1
                print(f"kast {cap}:", dg)

            values = dg.values()

            if play["bot"]:
                gained_points = Score_calculator.choose_score_bot(
                    values, playerid, playerboards, play["namn"]
                )
            else:
                gained_points = Score_calculator.choose_score_human(
                    values, playerid, playerboards
                )

            play["poang"] = Scoreboard.total_score(playerboards[playerid])

            print(f"\n{play['namn']} fick {gained_points} poäng denna runda.")
            Scoreboard.print_scoreboard(playerboards[playerid], play["namn"])
            print(f"{play['namn']} har nu totalt {play['poang']} poäng!")

    print("\n----------------------------------")
    print(f"SLUTRESULTAT: {play['poang']}")
    print("----------------------------------\n")

    
    for play in player_list:
        playerid = play["id"]
        play["poang"] = Scoreboard.total_score(playerboards[playerid])

    ranking = sorted(player_list, key=lambda p: p["poang"], reverse=True)

    placering = 1
    for play in ranking:
        print(play["namn"] + " - " + str(play["poang"]) + " poäng")
        placering += 1

    vinnare = ranking[0]
    forlorare = ranking[-1]

    print("\nFörsta plats: " + vinnare["namn"] + " - Vinnare med " + str(vinnare["poang"]) + " poäng")
    print("Sista plats: " + forlorare["namn"] + " - Förlorare med " + str(forlorare["poang"]) + " poäng")
    
    
    spara = input("Vill du spara yatzy spelet i en textfil? ")

    if spara.lower() == "ja":
        with open("yatzy_spel.txt", "w") as fil:

            fil.write("YATZY SPELRESULTAT\n")
            fil.write("----------------------\n\n")

        
            for play in player_list:
                playerid = play["id"]

                fil.write("Spelare: " + play["namn"] + "\n\n")
                fil.write("----------------------\n")

                board = playerboards[playerid]

                for kategori in board:
                    poang = board[kategori]
                    poang_text = str(poang) if poang is not None else "-"
                    fil.write(kategori + ": " + poang_text + "\n")

                total = Scoreboard.total_score(board)
                fil.write("TOTAL: " + str(total) + " poäng\n\n")

        
            fil.write("SLUTRESULTAT FÖR OMGÅNGEN\n")
            fil.write("----------------------\n")

            placering = 1
            for play in ranking:
                rad = str(placering) + ". " + play["namn"] + " - " + str(play["poang"]) + " poäng\n"
                fil.write(rad)
                placering += 1

            vinnare = ranking[0]
            fil.write("\nVinnare: " + vinnare["namn"] + "\n")
            print("SPELRESULTATET ÄR UTSKRIVEN I TEXTFILEN 'yatzy_spel.txt'")
    else:
        print("Tack för att du spelade yatzy!")
