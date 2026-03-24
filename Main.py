# -*- coding: utf-8 -*-

from Dicegroup import DiceGroup #Dicegroup skapar 5 tärningar
import Score_calculator #Lägger upp funktioner för poängalternativ, samt tar ut poäng
import Scoreboard #Skapar tombräda, lagrar spelarnas poäng
from Player import player_maker #Initierar spelare och botar

#Funktionen kollar när spelet är klart eller inte
#Det kollas genom att se kolla om None fortfarande är kvar i spelbrädan
#Om den är så retuneras: False --> Fortsätt
def all_scoreboards_filled(playerboards):
    for board in playerboards.values():
        if None in board.values():
            return False
    return True


if __name__ == "__main__":
    
#Kör funktionen player_maker() 
    player_list = player_maker()

    names = [p["namn"] for p in player_list]

#Kollar om det är 1, 2 eller flera spelare så att utskriften blir snygg
    if len(names) == 1:
        welcome = names[0]
    elif len(names) == 2:
        welcome = f"{names[0]} och {names[1]}"
    else:
        welcome = ", ".join(names[:-1]) + " och " + names[-1]

#Skriver ut välkommen till alla som ska spela
    print("\n----------------------------------")
    print(f"Välkommen {welcome}, till Yatzy!")
    print("----------------------------------\n")


#Skapar nu en spelbräda till x antal spelare som är kopplad via id
    playerboards = Scoreboard.create_playerboards(player_list, Score_calculator.fd)

#Denna del kollar bara spelbrädan individuellt för varje spelare som kör
#Om ens spelbärda är ifyilld så hoppar programmet över den spelaren
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
#Boten kastar alla 3 tärningar direkt
                if play["bot"]:
                    dg.roll()
                    cap += 1
                    print(f"Botkast {cap}: {dg}")
                    continue

#Här kommer det mer mänskliga spelet
#Kan spara de träningar man vill eller kasta om alla
                choice = input(info)


                if choice.lower() == "q":
                    print(f"{play['namn']} gav upp rundan")
                    break

#Om inte spelaren trycker 'Enter' --> sparat tärningar
#Programmet visualiseras vilka träningar som hålls och vilka som kommer att kastas
                if choice != "":
                    choice_clean = choice.replace(" ", "")
                    for ch in choice_clean:
                        if ch.isdigit():
                            n = int(ch) - 1
                            if n >= 0 and n <= 4:
                                dg.hold(n)
                    print("Tärningarna du håller: ", dg)


                dg.roll()
                cap += 1    
            values = dg.values()


#Dessa if - satser kollar helt enkelt om det är en bot eller människa
#Om bot välj bästa poängalternativet
#Annars låt människan välja vilken kategori
            if play["bot"]:
                gained_points = Score_calculator.choose_score_bot(
                    values, playerid, playerboards, play["namn"]
                )
            else:
                gained_points = Score_calculator.choose_score_human(
                    values, playerid, playerboards
                )

#Räknar totala poängen för spelaren hittils
#Inkluderat med bonus om man nu får bonus
            play["poang"] = Scoreboard.total_score(playerboards[playerid])

#Visar den resterande spelbrädan för just den spelaren
            Scoreboard.print_scoreboard(playerboards[playerid], play["namn"])
            print(f"{play['namn']} har nu totalt {play['poang']} poäng!")



    print("\n----------------------------------")
    print("SLUTRESULTAT ÄR FÖLJANDE:")
    print("----------------------------------\n")

 
    for play in player_list:
        playerid = play["id"]
        play["poang"] = Scoreboard.total_score(playerboards[playerid])

#Gör en funktion som hämtar poängen åt oss till rankning
    def get_score(p):
        return p["poang"]

    rankning = sorted(player_list, key=get_score, reverse=True)


#Skriver ut rankningen för hela spelomgången
    placering = 1
    for play in rankning:
        print(play["namn"] + " - " + str(play["poang"]) + " poäng")
        placering += 1

    vinnare = rankning[0]
    forlorare = rankning[-1]

#Skriver snyggt ut vem som vann och vem som förlorade spelet
    print("\nFörsta plats: " + vinnare["namn"] + " - Vinnare med " + str(vinnare["poang"]) + " poäng")
    print("Sista plats: " + forlorare["namn"] + " - Förlorare med " + str(forlorare["poang"]) + " poäng")
    

#Frågar användaren om du vill spara spelomgången i en textfil
#Om den vill så sparas hela spelrundan i "yatzy_spel.txt"
    spara = input("Vill du spara yatzy spelet i en textfil? Svara med 'ja' eller nej! ")

    if spara.lower() == "ja":
        with open("yatzy_spel.txt", "w") as fil:

            fil.write("YATZY SPELRESULTAT\n")
            fil.write("----------------------\n")

#Skriver ut vilka spelare har spelet        
            for play in player_list:

                fil.write("Spelare: " + play["namn"] + "\n")
            fil.write("----------------------\n")

       
            fil.write("SLUTRESULTAT FÖR OMGÅNGEN\n")
            fil.write("----------------------\n")

#Skriver ut alla spelare på en topplista
            placering = 1
            for play in rankning:
                rad = str(placering) + ". " + play["namn"] + " - " + str(play["poang"]) + " poäng\n"
                fil.write(rad)
                placering += 1

#Skriver ut vinnaren och förloraren som i konsolen
            fil.write("\nFörsta plats: " + vinnare["namn"] + "\n")
            fil.write("Sista plats: " + forlorare["namn"])
            print("SPELRESULTATET ÄR UTSKRIVEN I TEXTFILEN 'yatzy_spel.txt'")
    
    elif spara.lower() == "nej":
        print("Tack för att du spelade yatzy. Ha en bra dag, helg, lov eller liknade!")
        
    else:
        print("Ehhh?? Det var varken ja eller nej, men ha en bra dag")
