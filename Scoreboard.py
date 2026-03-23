# -*- coding: utf-8 -*-

#Här skapas en tom "spelbräda" för varje spelare och bot som ska spela
#Alla kategorier sätts till None
def make_empty_scoreboard(fd):
    return {key: None for key in fd.keys()}


#Här så blir varje spelare signerad sitt tomma spelbärda
#Notera att funktionen över gjorde endast en spelbärda som är tom
#Medan denna signerar den tomma spelbrädan till repsktive spelare och bot
def create_playerboards(player_list, fd):
    playerboards = {}

    for play in player_list:
        playerid = play["id"]
        playerboards[playerid] = make_empty_scoreboard(fd)

    return playerboards


#Denna funktion räknar ihop funktionerna ettor - sexor
#Om den är över så kommer en bonus ges till spelarne på 50
def upper_section_total(playerboard):
    keys = ["Ettor", "Tvåor", "Treor", "Fyror", "Femmor", "Sexor"]
    total = 0

    for key in keys:
        value = playerboard[key]
        if value is not None:
            total += value

    return total

#Delar upp det för att ena funktionen räknar poängen
#Den andra avgöra om spelaren faktiskt ska få det eller inte
def bonus_score(playerboard):
    if upper_section_total(playerboard) >= 63:
        return 50
    return 0

#Räknar bara ihop alla poäng för allt med bonusen inkluderad
def total_score(playerboard):
    total = 0

    for value in playerboard.values():
        if value is not None:
            total += value
            
#Här sker bonus tilläget om det nu isfålla sker
    total += bonus_score(playerboard)
    return total


#Gör det bara snyggt genom att skriva vemas spelbärda är vems
#Skriver ut spelbrädan oavsett om man inte har något namn (Man kan vill vara anonym)
def print_scoreboard(playerboard, namn):
    if namn != "":
        print(f"\nScoreboard för {namn}:")
    else:
        print("\nScoreboard:")

#Loopar igenom alla kategorier i spelbrädan och om de är none så blir det en utskrift på "Ej vald"
#Om den är vald så skriva kategorin ut samt värdet på den kategorin
    for key, value in playerboard.items():
        if value is None:
            print(f"{key}: Ej vald")
        else:
            print(f"{key}: {value}")

#Här så checkas bara om bonus poängen har blivit tillagd eller inte, för snyggheten skull
    print(f"Bonus: {bonus_score(playerboard)}")
#Visar total poängen efter varje omgång så spelaren vet utan att behöva räkna sjävl sitt totala poäng
    print(f"Total poäng: {total_score(playerboard)}")
