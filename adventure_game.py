# Hi there,
# Welcome to my little adventure game.
# I'd like to call it, "Drunk and Dangerous".
# You wake up in a field, or a barn.
# You are freezing to death, and have no idea where you are.
# You have to find your phone, but first your pincode, in that order!
# To do so, one can choose at the beginning between the farmer and the priest.
# The farmer has the phone, the priest the pincode.
# In this game there are different random situations and choices to be made.
# I hope you like it.

import time  # Import the time module
import random  # Import the random module


pincode = []  # To create a list.
# This list is to check if the player has the pincode once he finds the phone.
pincode_random = random.randint(4110, 4120)
# Create a global pincode variable for the pincode game, but only 10 options.
choice_random_coin = random.choice(("head", "tale"))
# Create a global variable for the coin toss game.


def intro():  # A function for the introduction scene.
    # It uses 3 scenarios as the opening line.
    print_pause(random.choice(("You wake up, it's dark, but the sun is rising",
                "A goat licks your face, you are in a field,\
in the middle of nowhere",
                              "You are in a barn, a door opens,\
all you see is a gun, you start to run, as fast as you can")))
    print_pause("You look around you but have no clue \
where you are, it's freezing")
    print_pause("Rumour has it, you drank a little to much")
    print_pause("Time to get up, and get home, you are starting to \
lose feelings in your feet and hands, hurry!")
    print_pause("But wait, where am I? And where is my phone? \
I need to call for help")
    print_pause("You see a farmer and a priest, let's ask them!\n")
    intro_choice()


def print_pause(message):  # Create a function to reduce duplications in code
    print(message)
    time.sleep(3)


def play_again():  # Create a function to ask whether
    # a player wants to play again or not.
    choice_play_again = input("Do you want to play again? \
Please answer with yes or no\n")
    if choice_play_again == "yes" or "no":
        if choice_play_again == "yes":
            print_pause("Allright, buckle up!")
            time.sleep(5)
            start_game()
        else:
            print_pause("Thanks for playing!")
    else:
        print_pause("I don't understand you")
        play_again()


def game_dial_number():  # Creates a function with 3 dial variables.
    # 1 and 2 will cause the player to win.
    # Choosing 3 will cause the player to lose.
    game_dial_choice = int(input("Who do you dial? Please press 1, 2 or 3\n"))
    if game_dial_choice == 1:
        print_pause("You dial 1, it's your mother, she quickly \
comes to rescue you, you won!")
        play_again()
    elif game_dial_choice == 2:
        print_pause("You dial 2, it's the police, they quickly come to \
 rescue you with a paramedic helicopter, you won!")
        play_again()
    elif game_dial_choice == 3:
        print_pause("You dial 3, it's your ex, she tells you \
you are joking and hangs up.\n")
        print_pause("You feel you are losing breath and fall down.")
        print_pause("Game over")
        play_again()
    else:
        print_pause("You pressed the wrong button")
        game_dial_number()


def play_pincodegame():  # Creates a function for the pincode game.
    choice_number = int(input("Guess your pincode, \
if it's correct, I will let you know\n"))
    if pincode_random != choice_number:
        # print(pincode_random) -> can be turned off/on during test runs.
        print_pause("try again, remember it starts with 411")
        time.sleep(0.5)
        play_pincodegame()
    else:
        print_pause("That's correct, your pincode = " + str(choice_number))
        print_pause("Thank god, you have your pincode")
        print_pause("you walk back to the road, let's find your phone!")
        print_pause("Hmm, back at the starting point, so the priest \
knew my pincode, what would the farmer know?\n")
        pincode.append("pin")
        intro_choice()


def intro_choice():  # Creates a function to use when
    # the player returns to the field or barn.
    choice_intro = input("who do I choose? Please enter farmer or priest\n")
    if choice_intro == "farmer":
        print_pause("\nYou see the farmer, he walks towards you: 'Hi there \
young fellow, had a tough night?  I'm on my morning walk,")
        print_pause("and I happened to find a phone a few minutes back, \
is it yours? I will tell you the location, \
if you play a game with me.'")
        play_game_farmer()
    elif choice_intro == "priest":
        print_pause("You see the priest, with respect you approach him")
        print_pause("He sees you: 'Hi there, are you the boy of the \
lost phone?'")
        play_game_priest()
    else:
        print_pause("What do you mean?")
        intro_choice()


def unlock_phone():  # Creates a function for the unlocking phone scene.
    # If the player does not have the pincode yet,
    # he will be to late to call rescue and freeze to death.
    print_pause("Your fingers are so frozen, the fingerlock doesn't \
work anymore\n")
    if "pin" in pincode:
        print_pause("wait, didn't the priest gave you the pincode!")
        print_pause("He did, your phone unlocks!")
        print_pause("You feel you are dying, losing breath")
        print_pause("Your fingers are so frozen, you must dial quickly")
        game_dial_number()
    else:
        print_pause("You drank so much last night, that you forgot \
your pincode")
        print_pause("You fall down, if only somehow you knew your pincode")
        print_pause("it's too late, you start to lose your breath\n")
        print_pause("Game over\n")
        play_again()


def mobile_location():  # The mobile location scene.
    print_pause("The old man sighs, okay, I will tell you")
    print_pause("If you walk 5 miles back, there is your phone, good luck\n")
    print_pause("You walk, barely have feelings in your feet")
    print_pause("It freezes, but there it is! Your phone\n!")
    unlock_phone()


def play_coingame():  # Creates a function to play the head/tale game
    choice_dicegame = input("\nWhat do you choose, head or tale?\n")
    if choice_dicegame == "head" or "tale":
        if choice_random_coin == choice_dicegame:
            print_pause("\nYou Won!\n")
            mobile_location()
        else:
            print_pause("You lost, try again")
            play_coingame()
    else:
        print_pause("I don't understand you")
        play_coingame()


def play_game_farmer():  # Creates a function for the farmer scene
    choice_game = input("\nWill you play the game? \
please answer with yes or no\n")
    if choice_game == "yes":
        print_pause("\nexcellent")
        print_pause("The game is a classic head/tale.")
        play_coingame()
    elif choice_game == "no":
        print_pause("Good luck with finding your phone, bye")
        print_pause("You walk back to the road")
        print_pause("You look around you,\
the only people you see are the priest and the farmer \
They must know more")
        intro_choice()
    else:
        print_pause("I don't understand you?")
        play_game_farmer()


def play_game_priest():  # Creates a function for the priest scene
    print_pause("Welcome, I am the priest")
    print_pause("The wind told me you lost your phone and pincode")
    print_pause("I happen to have found a little note with a pincode.")
    print_pause("You have to earn it back, lets play a guess game")
    print_pause("To make it easier, I will show you 3 of the 4 numbers")
    print_pause("The numbers are: 411*")
    play_pincodegame()


def start_game():  # Creates a function to start the game.
    intro()


start_game()
