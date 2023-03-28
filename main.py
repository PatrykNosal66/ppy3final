#numbers = input("Wprowadź liczby, oddzielając je przecinkiem: ")
#numbers_list = numbers.split(",")
#min= int(numbers_list[0])
#max = int(numbers_list[0])
#for num in numbers_list:
#    num = int(num)
#    if num < min:
#        minimum = num
#    if num > max:
#        max = num
#print("Minimum:", min)
#print("Maksimum:", max)

#========================================================================


#import random

#miasta = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

#odwiedzone_miasta = []

#while len(odwiedzone_miasta) < 10:  # dopóki nie odwiedzono 10 miast
#    miasto = random.choice(miasta)  # losuje miasto
#    if miasto not in odwiedzone_miasta:  # jeśli miasto nie było wcześniej odwiedzone
#        odwiedzone_miasta.append(miasto)  # dodaje miasto do listy odwiedzonych

#print("Plan wycieczki:")
#for i, miasto in enumerate(odwiedzone_miasta):
#    print(f"{i+1}. {miasto}")




#=================================================================================
if(2==2):
    import random
    from getpass import getpass


    def get_player_choice(player_name):
        while True:
            choice = getpass(f"{player_name}, wybierz papier, nożyce lub kamień: ")
            if choice.lower() in ["papier", "nożyce", "kamień"]:
                return choice.lower()
            print("Nieprawidłowy wybór, spróbuj ponownie.")


    def get_computer_choice():
        return random.choice(["papier", "nożyce", "kamień"])


    def play_round(player1, player2):
        if player2 == "komputer":
            player2_choice = get_computer_choice()
        else:
            player2_choice = get_player_choice(player2)

        player1_choice = get_player_choice(player1)

        if player1_choice == player2_choice:
            return "remis"
        elif (player1_choice == "papier" and player2_choice == "nożyce" or
              player1_choice == "nożyce" and player2_choice == "kamień" or
              player1_choice == "kamień" and player2_choice == "papier"):
            return player2
        else:
            return player1


    def print_results(results):
        print("Wyniki poszczególnych rund:")
        for i, result in enumerate(results):
            print(f"Runda {i + 1}: {result}")


    def print_final_results(results, player1, player2):
        player1_score = results.count(player1)
        player2_score = results.count(player2)
        if player1_score > player2_score:
            print(f"{player1} wygrał grę z wynikiem {player1_score}:{player2_score}!")
        elif player1_score < player2_score:
            print(f"{player2} wygrał grę z wynikiem {player2_score}:{player1_score}!")
        else:
            print("Remis!")







    num_rounds = int(input("Wybierz liczbę rund: "))

    if input("Czy chcesz grać z SI? (tak/nie): ").lower() == "tak":
        player1 = input("Podaj swoje imię: ")
        player2 = "SI"
    else:
        player1 = input("Podaj imię pierwszego gracza: ")
        player2 = input("Podaj imię drugiego gracza: ")

    results = []
    for i in range(num_rounds):
        print(f"Runda {i + 1}:")
        winner = play_round(player1, player2)
        results.append(winner)
        if winner == "remis":
            print("Remis!")
        else:
            print(f"{winner} wygrał!")

    print_results(results)
    print_final_results(results, player1, player2)

