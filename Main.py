# -*- coding: utf-8 -*-
#importerar våra klasser
from Dicegroup import DiceGroup #dicegroup skapar 5 tärningar
import Score_calculator #lägger upp funktioner för poängalternativ, samt tar ut poäng
import Scoreboard #skapar tombräda, lagrar spelarnas poäng
from Player import player_maker #initierar spelare och botar

#en funktion som checkar ifall alla spelare fyllt i sin information som namn men även poäng för deras turer
def all_scoreboards_filled(playerboards):
    for board in playerboards.values():
        if None in board.values():
            return False
    return True

#gör spelkare och gör roliga meddlanden
if __name__ == "__main__":
    player_list = player_maker()

    names = [p["namn"] for p in player_list]

    if len(names) == 1:
        welcome = names[0]
    elif len(names) == 2:
        welcome = f"{names[0]} och {names[1]}"
    else:
        welcome = ", ".join(names[:-1]) + " och " + names[-1]
        #här ärre mest bara grejer som hanterar ifall de typ är flera namn osv
        
    #här är ett kul meddelande som gör det lite fuint
    print("\n/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\n")
    print(f"Välkomna {welcome}!\n")
    print("\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\n")
    #spelarnas scoreboards samlas
    playerboards = Scoreboard.create_playerboards(player_list, Score_calculator.fd)
    #en simpel loop här som checkar när det är nåns tur med hjälp av filled fucntionen
    while not all_scoreboards_filled(playerboards):
        for play in player_list:
            playerid = play["id"]

            if None not in playerboards[playerid].values():
                continue
            #kul meddelande för turer
            print("\n----------------------------------")
            print(f"Det är {play['namn']}s tur!")
            print("----------------------------------\n")

            dg = DiceGroup()

            #första kastet körs direkt så man inte behöver trycka massa i onödan
            dg.roll()
            cap = 1
            print("första kastet:", dg)

            info = "Välj vilka tärningar du vill behålla (1-5) eller tryck Enter för att kasta igen: "

            while cap < 3:
                if play["bot"]:
                    dg.roll()
                    cap += 1
                    print(f"Robotkast {cap}: {dg}")
                    continue

                choice = input(info)
                #q för att ge upp rundan
                if choice.lower() == "q":
                    print(f"{play['namn']} gav upp rundan")
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
                cap += 1
                print(f"Efter kast {cap}:", dg)

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
            print(f"{play['namn']} har nu totalt {play['poang']} poäng.")
            #kul meddelande
    print("\n\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/")
    print("\nSLUTRESULTAT:")
    print("\n/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\n")

    #uppdatera totalscore en sista gång så bonus säkert räknas in korrekt
    for play in player_list:
        playerid = play["id"]
        play["poang"] = Scoreboard.total_score(playerboards[playerid])
    #gör en funktion  som hämtar poängen åt oss till rankingen
    def get_score(p):
        return p["poang"]
    
    ranking = sorted(player_list, key=get_score, reverse=True)
    #printar scores
    for i, play in enumerate(ranking, start=1):
        print(f"{i}. {play['namn']} - {play['poang']} poäng")

    print(f"\nFörsta plats: {ranking[0]['namn']} - WINNARE med {ranking[0]['poang']} poäng")
    print(f"Sista plats: {ranking[-1]['namn']} - FÖRLORARE med {ranking[-1]['poang']} poäng")
