# -*- coding: utf-8 -*-

def player_maker():
    while True:
        try:
            antal_manniskor = int(input("Hur många mänskliga spelare ska spela? "))
            if antal_manniskor >= 0:
                break
            else:
                print("Antalet kan inte vara negativt.")
        except ValueError:
            print("Skriv ett heltal.")

    while True:
        try:
            antal_botar = int(input("Hur många botar ska spela? "))
            if antal_botar >= 0:
                break
            else:
                print("Antalet kan inte vara negativt.")
        except ValueError:
            print("Skriv ett heltal.")

    if antal_manniskor == 0 and antal_botar == 0:
        print("Minst en spelare måste finnas.")
        return player_maker()

    player_list = []

    for i in range(antal_manniskor):
        namn = input(f"Skriv namn på spelare {i+1}: ")
        player_list.append({
            "id": len(player_list),
            "namn": namn,
            "poang": 0,
            "bot": False
        })

    for i in range(antal_botar):
        namn = f"Robotpojken{i+1}"
        player_list.append({
            "id": len(player_list),
            "namn": namn,
            "poang": 0,
            "bot": True
        })

    return player_list
