from random import seed
from random import randrange
from datetime import datetime

seed(int(datetime.timestamp(datetime.now())))


computer_wins = 0
user_wins = 0
rounds = 0
history = []

print("Welcome to the rock paper scissor game")
while computer_wins < 3 and user_wins < 3:
    user = input("Please choose rock, scissor or paper: ")
    rounds += 1
    print("\n")
    print("Round " + str(rounds))
    while user not in ["rock","scissor","paper"]:
        user = input("Please try again between rock, scissor, paper :")


    #computers choice
    pc = randrange(3)
    if pc == 0:
        computer = "paper"
    elif pc == 1:
        computer = "rock"
    else:
        computer = "scissor"

    if user == "paper" and computer == "rock":
        winner = "User"
        user_wins += 1
    elif user == "rock" and computer == "scissor":
        winner = "User"
        user_wins += 1
    elif user == "scissor" and computer == "paper":
        winner = "User"
        user_wins += 1
    elif user == "paper" and computer == "scissor":
        winner = "Computer"
        computer_wins += 1
    elif user == "rock" and computer == "paper":
        winner = "Computer"
        computer_wins += 1
    elif user == "scissor" and computer == "rock":
        winner = "Computer"
        computer_wins += 1
    else:
        winner = "Its a tie"
    print("You chosen: " + user + " computer chosen: " + computer)
    print("The score for user - computer is " + str(user_wins) + " - " + str(computer_wins))
    print("==================================\n")

    #update of history
    history.append("Round " + str(rounds) + ":User:" + user + "," + "Computer: " + computer + ":" + str(user_wins)
                   + "-" + str(computer_wins))

#display the winner
if user_wins == 3:
    print("User has was with " + str(user_wins) +" "+ str(computer_wins))
    for elem in history:
        print(elem)
elif computer_wins == 3:
    print("Computer has won with " + str(computer_wins) +" "+ str(user_wins))
    for elem in history:
        print(elem)
