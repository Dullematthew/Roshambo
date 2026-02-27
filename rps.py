# create a rock, paper, scissor game
import random
from colorama import init, Fore
init(autoreset=True)
choices = ["rock", "paper", "scissors"]
print("Welcome to Roshambo! Can you beat me?")
wincounter = 0
playerscore = 0
computerscore = 0
while True:
    # add a score
    print(f"Your score: {playerscore}|Computer: {computerscore} \n")
    # need to be able to take users input so they can select
    player = input("Choose either rock, paper, or scissors:")
    #need to give random choice to computer
    computer = random.choice(choices)
    print("Your opponent chooses:", computer)
    if computer == player:
        print(Fore.BLUE+"Its a Tie")
        wincounter = 0
    elif computer == "rock" and player == "paper":
        print(Fore.GREEN+"You Win!")
        wincounter += 1
        playerscore += 1
    elif computer == "paper" and player == "rock":
        print(Fore.RED+"You Lose!")
        wincounter = 0
        computerscore += 1
    elif computer == "rock" and player == "scissors":
        print(Fore.RED+"You Lose!")
        wincounter = 0
        computerscore += 1
    elif computer == "paper" and player == "scissors":
        print(Fore.GREEN+"You Win!")
        wincounter += 1
        playerscore += 1
    elif computer == "scissors" and player == "paper":
        print(Fore.RED+"You Lose!")
        wincounter = 0
        computerscore += 1
    elif computer == "scissors" and player == "rock":
        print(Fore.GREEN+"You Win!")
        wincounter += 1
        playerscore += 1
    elif player == "gun":
        print(Fore.GREEN+"Woah, woah, woah, no need to escalate things")
        wincounter += 1
        playerscore += 1
    else: 
        print("Thats not an option! Please try again")
    print(Fore.YELLOW+"Win Streak:", wincounter)
    play = input("Would you like to play again (Y/N)")
    if play == "Y":
         print("Thanks for playing, Lests go another round!")
            
    elif play == "N":
        print("Good game! Have a good one!")
        break
 
    
