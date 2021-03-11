# Importing required modules
from emojis import encode as emoji
from random import choice as choose
from time import sleep as wait

# Printing instructions
print(f"Welcome to Snake({emoji(':snake:')}), Water({emoji(':ocean:')}), Gun({emoji(':gun:')})!")
print("The respective codes are--> ")
print(f"{emoji(':snake:')} : 1")
print(f"{emoji(':ocean:')} : 2")
print(f"{emoji(':gun:')} : 3\n")

wait(0.7)

# Asking how many matches in a game 
total_games = int(input("How many times you wanna play? "))
print()

# Win-lose track dict
point_track = {
    'snake':{'snake':None, 'water':1, 'gun':0},
    'water':{'snake':0, 'water':None, 'gun':1},
    'gun':{'snake':1, 'water':0, 'gun':None}
}

choices = ['snake', 'water', 'gun']

user_points, computer_points = 0,0

print("Let's Begin!\n")
wait(0.5)


#Initiating the game
for counter in range(1, total_games+1):

    # Taking the choices and displaying them
    user_choice = choices[int(input("What do you choose (1/2/3): "))-1]
    computer_choice = choose(choices)

    wait(0.8)
    print("The computer chose", computer_choice)
    print("You chose", user_choice)


    # Distributing the points accordingly
    if point_track[user_choice][computer_choice] == 1:
        print(f"You won! {emoji(':smile:')}")
        user_points+=1

    elif point_track[user_choice][computer_choice] == 0:
        print(f"Computer won! {emoji(':pensive:')}")
        computer_points+=1

    elif point_track[user_choice][computer_choice] == None:
        print(f"Tie! {emoji(':dizzy:')}")

    else: print("You lost a turn due to invalid input...")

    wait(0.5)
    print(f"\nRounds left: {total_games-counter}\n")

# Giving the final judgement
print("The final judgement is... ==>")
wait(1)

print(f"Computer scored {computer_points} points.")
print(f"You scored {user_points} points.\n")

print(f"You won! {emoji(':fire:')}") if user_points>computer_points else print(f"Computer won! {emoji(':smirk:')}") if user_points<computer_points else print(f"Tie! {emoji(':dizzy:')}")