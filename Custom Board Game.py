
import random
import time 







# This initializes the player's starting locations
current_player_location = 1
location1 = 1
location2 = 1
current_player = 1 


# Ask once for the dice type
dice_sides = int(input("Choose the dice type for the game (6 , 7 or 8): "))




# Function to execute a turn for the current player
def turn(current_player, current_player_location, dice_sides): 
        # Prompt the player to roll the dice
        print(f'{current_player} please roll the dice by clicking the enter button. ')
        input('')
        dice = random.randint(1, dice_sides)
        print(f' You rolled a {dice}')
        # Update player location based on dice roll
        current_player_location = current_player_location + dice
        print(f' You are now on square, {current_player_location}')
        # Check for speical squares and the sqaure's corresponding effects
        if current_player_location == 5 or current_player_location == 25:
            current_player_location = current_player_location + 3
            print('You are going forwards 3 spaces!!! ')
        elif current_player_location == 6 or current_player_location == 26:
            current_player_location = current_player_location - 5
            print('Unlucky, you are going back to the start! ')
        elif current_player_location == 14 or current_player_location == 34:
            current_player_location = current_player_location - 3
            print('Tough luck! You are going back 3 spaces!!! ')
        elif current_player_location == 18 or current_player_location == 38:
            current_player_location = current_player_location - 2
            print('Unlucky, you are going back 2 spaces!!! ')
        elif current_player_location == 19 or current_player_location == 39:
            current_player_location = current_player_location - 4
            print('Bad luck. You are going back 4 spaces!! ')
        elif current_player_location == 20 or current_player_location == 40:
            print('You are now on position 20!!! ')
            decision = int(input('Choose a number from 1 to 6 to move forwards or backwards. Choose wisely!!!:  '))
            if decision == 1:
                print('Lucky! You are going to go forwards 1 space! ')
                current_player_location = current_player_location + 1
            elif decision == 2:
                print('Better luck next time! You are going to go backwards 2 spaces!')
                current_player_location = current_player_location - 2
            elif decision == 3:
                print('Good job! You are going to go forwards 3 spaces!')
                current_player_location = current_player_location + 3
            elif decision == 4:
                print('Tough luck! Unfortunately, you are going to go back 4 spaces! ')
                current_player_location = current_player_location - 4
            elif decision == 5:
                print('Today is your lucky day! You are going to go forwards 5 spaces! ')
                current_player_location = current_player_location + 5
            elif decision == 6:
                print('Today is not your day is it? You are going to back 6 spaces! ')
                current_player_location = current_player_location - 6
            else:
                print('Please enter a valid number. ')
        # Return the updated location 
        return current_player_location




# The welcome messages, and introductory phase
print("""┌───────────────────────────────────────┐
│WELCOME TO THE BOARD GAME PLAYERS!!!!!!│
└───────────────────────────────────────┘""")
print("""How to play the game:
      1. First player to go around the game board 2 times (That is 40 sqaures in total) wins the game!
      2. Be careful of some of the squares!!!!!!!!!
      Good Luck!!!!!!
""")
player1 = input('Please enter your name: ')
player2 = input('Please enter your name: ')

location1, location2 = 1, 1
winner = None


# This is the main game loop
while winner is None:
    if current_player == 1:
        location1 = turn(player1, location1, dice_sides)
        if location1 >= 40:
            winner = player1
        else:
            current_player = 2
    else:
        location2 = turn(player2, location2, dice_sides)
        if location2 >= 40:
            winner = player2
        else:
            current_player = 1





# Annoncing the winner and end of the game 
print(f" Congratulations {winner}, you have won the game!")
print("""┌──────────────────────────────┐
│Congratulations Winner!!!!!!!!│
└──────────────────────────────┘""")

   





