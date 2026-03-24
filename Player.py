# -*- coding: utf-8 -*-

#Programmet frågar användaren hur många "mänskliga" spelare ska spela
#Vi kollar med if - stasen om användaren väljer spelare eller ej
#Vi har även en try-sats som checkar om vi skriver ett heltal
def player_maker():
    while True:
        try:
            antal_manniskor = int(input("Hur många människor ska spela? "))
            if antal_manniskor >= 0:
                break
            else:
                print("Negativt? Du kan inte ha negativt med männsikor...?")
        except ValueError:
            print("Skriv ett heltal!")
            
#Samma sak sker här som på funktionen över, fast programmet frågar bara efter botar 
    while True:
        try:
            antal_botar = int(input("Hur många botar ska spela? "))
            if antal_botar >= 0:
                break
            else:
                print("Du kan inte ha negativt med botar...?")
        except ValueError:
            print("Skriv ett heltal!")

#Kollar om inputen från användaren är 0 på mänskliga och botar
#Om den är så skickas användaren till starten igen och blir frågade om antal spelare
    if antal_manniskor == 0 and antal_botar == 0:
        print("Det måste finnas minst en spelare i spelomgången")
        return player_maker()

    player_list = []

#Ber användaren om deras namn
#Använder oss av ".title" så att användarens namn startar med en stor bokstav oavsett hur de skriver
    for i in range(antal_manniskor):
        namn = input(f"Vad heter du? {i+1}: ").title()
#Lägger till namnet i vår tomma lista
        player_list.append({
#Här så kopplas id på spelaren namnet och deras poäng
#Till deras respektive egna spelbärda
#Detta gör så att respektiva spelare har sitt id länkat till sitt scoreboard
            "id": len(player_list),
            "namn": namn,
            "poang": 0,
            "bot": False
        })

#Samma ska sker här då vi döper botarna till bot_1, bot_2, bot_3 osv
#Sätter nyckeln "bot" --> True för då vet programmet att boten ska välja bästa möjliga poängalternativ
    for i in range(antal_botar):
        namn = f"Bot_{i+1}"
        player_list.append({
            "id": len(player_list),
            "namn": namn,
            "poang": 0,
            "bot": True
        })

    return player_list
