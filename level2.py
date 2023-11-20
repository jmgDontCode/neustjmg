import os
import time
import random

import keyboard

Character1 = "Michael"  # Character names,health,speed
Character2 = "Wholesome"
Character3 = "Undertaken"
Character4 = "Cena"
Character5 = "John"
MainPage = "Main Page"
Character1Health = 150
Character1Speed = 20
Character2Health = 150
Character2Speed = 25
Character3Health = 150
Character3Speed = 30
Character4Health = 150
Character4Speed = 35
Character5Health = 150
Character5Speed = 40  # Character names,health,speed

Player1Character = ""  # Player Character Info
Player1HP = 0
Player1Speed = 0
Computer1Character = ""  # Ai Character Info
Computer1HP = 0
Computer1Speed = 0
damage = 0

start = True  # To formally start the game
player_turn = True  # True = First to turn : Player / False = First to turn : Ai
# I use term "global" to make the values of a specific variables can use from function to function
print("Welcome to Slap me")
print("Press Space to Continue")

def start_game():
    while start:
        if keyboard.is_pressed("1"):
            print("SLAP ME !!!")
            print("[1] Start Game")
            print("[2] Characters Info")
            print("[3] Quit")
            userInput = input()
            if userInput == '1':
                userCharacter()
            elif userInput == '2':
                print("""A one-on-one slap contest between an AI and a player, where the player have the freedom to 
select their characters as well as select their enemies. The contest is divided into three rounds
and the outcome depends on the meter as well as the player’s strategy and skills. """)
                print("Press 1 to go back")
                userInput = input()
                if userInput == '1':
                    start_game()

            elif userInput == '3':
                print("Do you want to exit? [1] Yes [2] No")
                userInput1 = input()
                if userInput1 == '1':
                    quit()
                else:
                    start_game()


def userCharacter():                    # Selection for Player
    global Player1HP, Player1Speed, Player1Character
    menu = True
    while menu:
        os.system('cls')
        print("Please choose your Slapper")
        print("[1] ", Character1)
        print("[2] ", Character2)
        print("[3] ", Character3)
        print("[4] ", Character4)
        print("[5] ", Character5)
        print("[7] ", MainPage)
        Slapper = input()

        if Slapper == "1":
            print("Character 1 Selected")
            menu = False
            print("Health : ", Character1Health)
            print("Speed : ", Character1Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Player1Character = Character1
                Player1HP = Character1Health
                Player1Speed = Character1Speed
                aiCharacter()

            else:
                userCharacter()

        elif Slapper == "2":
            print("Character 2 Selected")
            menu = False
            print("Health : ", Character2Health)
            print("Speed : ", Character2Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Player1Character = Character2
                Player1HP = Character2Health
                Player1Speed = Character2Speed
                aiCharacter()
            else:
                userCharacter()
        elif Slapper == "3":
            print("Character 3 Selected")
            menu = False
            print("Health : ", Character3Health)
            print("Speed : ", Character3Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Player1Character = Character3
                Player1HP = Character3Health
                Player1Speed = Character3Speed
                aiCharacter()

            else:
                userCharacter()
        elif Slapper == "4":
            print("Character 4 Selected")
            menu = False
            print("Health : ", Character4Health)
            print("Speed : ", Character4Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Player1Character = Character4
                Player1HP = Character4Health
                Player1Speed = Character4Speed
                aiCharacter()

            else:
                userCharacter()
        elif Slapper == "5":
            print("Character 5 Selected")
            menu = False
            print("Health : ", Character5Health)
            print("Speed : ", Character5Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Player1Character = Character5
                Player1HP = Character5Health
                Player1Speed = Character5Speed
                aiCharacter()
            else:
                userCharacter()
                print("")
        elif Slapper == "7":
            print("Back to ", MainPage)
            menu = False
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                start_game()
            else:
                userCharacter()
        else:
            print("Invalid")
            userCharacter()


# Selection for Player

def aiCharacter():  # Selection for Ai
    global Computer1HP, Computer1Speed, Computer1Character
    menu = True
    while menu:
        os.system('cls')
        print("Please choose enemy Slapper")
        print("[1] ", Character1)
        print("[2] ", Character2)
        print("[3] ", Character3)
        print("[4] ", Character4)
        print("[5] ", Character5)
        print("[6] Back to Player Slapper Selection")
        print("[7] ", MainPage)

        SlapperAi = input()

        if SlapperAi == "1":
            print("Character 1 Selected")
            menu = False
            print("Health : ", Character1Health)
            print("Speed : ", Character1Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Computer1Character = Character1
                Computer1HP = Character1Health
                Computer1Speed = Character1Speed
                loading()
            else:
                aiCharacter()
        elif SlapperAi == "2":
            print("Character 2 Selected")
            menu = False
            print("Health : ", Character2Health)
            print("Speed : ", Character2Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Computer1Character = Character2
                Computer1HP = Character2Health
                Computer1Speed = Character2Speed
                loading()
            else:
                aiCharacter()
        elif SlapperAi == "3":
            print("Character 3 Selected")
            menu = False
            print("Health : ", Character3Health)
            print("Speed : ", Character3Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Computer1Character = Character3
                Computer1HP = Character3Health
                Computer1Speed = Character3Speed
                loading()
            else:
                aiCharacter()
        elif SlapperAi == "4":
            print("Character 4 Selected")
            menu = False
            print("Health : ", Character4Health)
            print("Speed : ", Character4Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Computer1Character = Character4
                Computer1HP = Character4Health
                Computer1Speed = Character4Speed
                loading()
            else:
                aiCharacter()
        elif SlapperAi == "5":
            print("Character 5 Selected")
            menu = False
            print("Health : ", Character5Health)
            print("Speed : ", Character5Speed)
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                Computer1Character = Character5
                Computer1HP = Character5Health
                Computer1Speed = Character5Speed
                loading()
            else:
                aiCharacter()
        elif SlapperAi == "6":
            print("Back to Player Slapper Selection")
            menu = False
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                userCharacter()
            else:
                print("Invalid")
                aiCharacter()
        elif SlapperAi == "7":
            print("Back to ", MainPage)
            menu = False
            confirmation = input("Are you sure? [1] Yes [2] No ")
            if confirmation == '1':
                start_game()
            else:
                print("Invalid")
                aiCharacter()


# Selection for Ai

print("")
print("")


def loading():  # Loading / Waiting for Battle
    global player_turn
    if Player1Speed > Computer1Speed:
        print(Player1Character, "VS. ", Computer1Character)
        time.sleep(0.5)
        print("Loading: Please Wait.")
        time.sleep(0.5)
        print("Loading: Please Wait..")
        time.sleep(0.5)
        print("Loading: Please Wait...")
        time.sleep(0.5)
        print("First Slapper is You")
        time.sleep(0.5)
        print("Match Starting in 3")
        time.sleep(0.5)
        print("Match Starting in 2")
        time.sleep(0.5)
        print("Match Starting in 1")
    else:
        print(Player1Character, "VS. ", Computer1Character)
        time.sleep(0.5)
        print("Loading: Please Wait.")
        time.sleep(0.5)
        print("Loading: Please Wait..")
        time.sleep(0.5)
        print("Loading: Please Wait...")
        time.sleep(0.5)
        print("First Slapper is your Enemy")
        time.sleep(0.5)
        print("Match Starting in 3")
        time.sleep(0.5)
        print("Match Starting in 2")
        time.sleep(0.5)
        print("Match Starting in 1")
        player_turn = False

    slap()


# Loading / Waiting for Battle

def display_meter(meter_value, max_value, length=30):  # Meter to Determine the impact damage
    ratio = meter_value / max_value
    num_ticks = int(length * ratio)
    num_spaces = length - num_ticks
    meter = "[" + "█" * num_ticks + " " * num_spaces + "]"
    print(f"\rProgress: {meter} ({meter_value}/{max_value})", end="")


def computer_attack():  # Ai meter attack
    global damage, Player1HP
    max_value = 100
    meter_value = 0
    direction = 1  # 1 for forward, -1 for backward

    while True:
        display_meter(meter_value, max_value)
        time.sleep(0.009)  # to change the speed of the meter

        if direction == 1:
            meter_value += 1
        else:
            meter_value -= 1

        if meter_value >= max_value:
            direction = -1
        elif meter_value <= 0:
            direction = 1

        if 0 <= meter_value <= 100:
            if random.random() < 0.010:  # this to make the AI use the meter timing
                break

    if meter_value <= 40:
        damage = 10
    elif meter_value <= 70:
        damage = 20
    elif meter_value <= 90:
        damage = 30
    elif meter_value <= 100:
        damage = 40


def player_attack():  # Player to attack
    global damage, Computer1HP
    max_value = 100
    meter_value = 0
    direction = 1  # 1 for forward, -1 for backward

    while True:
        display_meter(meter_value, max_value)
        time.sleep(0.009)  # to change the speed of the meter

        if direction == 1:
            meter_value += 1
        else:
            meter_value -= 1

        if meter_value >= max_value:
            direction = -1
        elif meter_value <= 0:
            direction = 1

        if keyboard.is_pressed("space"):  # to change to any key
            break

    if meter_value <= 40:
        damage = 10
    elif meter_value <= 70:
        damage = 20
    elif meter_value <= 90:
        damage = 30
    elif meter_value <= 100:
        damage = 40


def slap():  # para slap si player at ai ng back and fort
    global damage, Player1HP, Computer1HP, player_turn
    player_health = Player1HP
    ai_health = Computer1HP

    while player_health > 0 and ai_health > 0:
        if player_turn:
            print("\nYour turn:")
            time.sleep(1)
            player_attack()
            ai_health -= damage
            print(f"You slapped the AI for {damage} damage. AI's health: {ai_health}")
        else:
            print("\nAI's turn:")
            time.sleep(1)
            computer_attack()
            player_health -= damage
            print(f"The AI slapped you for {damage} damage. Your health: {player_health}")

        player_turn = not player_turn

    if player_health <= 0:
        print("YOU LOSE!")
        print("Play Again? [1] Yes [2] No")  # to make user choice if they want to player again or no
        confirmation = input()
        if confirmation == "1":
            userCharacter()
        else:
            start_game()
    else:
        print(" YOU WIN!!")
        print("Play Again? [1] Yes [2] No")
        confirmation = input()
        if confirmation == "1":
            userCharacter()
        else:
            start_game()


if __name__ == "__main__":
    start_game()
