from art import logo
import random

def Blackjack():

    game = True
    while game:
        quess = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ").lower()
        if quess == "y":

            print(logo)
            def card(gamer):
                CardsNumber = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                RandomChoice = random.choice(CardsNumber)
                gamer.append(RandomChoice)
                return gamer
            def total(cardNumber):
                totalNumber = sum(cardNumber)
                return totalNumber


            #create player and player's score
            player = []

            #create computer and computer's score
            computer = []


            cards = True
            while cards:
                if len(player) and len(computer) == 2:
                    cards= False

                else:
                    card(player)
                    card(computer)


            print(f"Your cards: {player}, Score: {total(player)}")
            print(f"Computer's cards: first card: {computer[0]}")

            add_card = True
            while add_card:
                continue_question = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if continue_question == "y":
                    card(player)
                    print(f" Player card: {player} Score: {total(player)}")
                    print(f" Computer firs card: {computer[0]}")
                    if total(player) > 21:
                        print(f" Player card: {player}, Score: {total(player)}")
                        print(f" Computer card: {computer}, Score: {total(computer)}")
                        print("Computer Win !! forget the chicken")

                        add_card = False

                    elif total(computer) < 17:
                        card(computer)
                        if total(computer) > 21:
                            print(f" Player card: {player}, Score: {total(player)}")
                            print(f" Computer card: {computer}, Score: {total(computer)}")
                            print("Winner Winner Chicken Dinner !!")
                            add_card = False

                elif continue_question == "n":
                    print(f" Player card: {player}, Score: {total(player)}")
                    print(f" Computer card: {computer}, Score: {total(computer)}")
                    if total(player) > total(computer):
                        print("Winner Winner Chicken Dinner !!")
                        add_card = False
                    elif total(player) == total(computer):
                        print("DRAW !!")
                        add_card = False
                    else:
                        print("Computer Win !! forget the chicken")
                        add_card = False
        elif quess == "n":
            break

Blackjack()