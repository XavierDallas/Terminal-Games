import random
import time

options = ["rock", "paper", "scissors"]
player_score = 0
opponent_score = 0
gameSTARTchoice =" "
player_choice = ""
opponent_choice = ""

def menu():
    global gameSTARTchoice
    gameSTARTchoice =" "
    print("Welcome to Rock Paper Scissors:")
    time.sleep(1)
    print("To begin please input Y")
    time.sleep(1)
    while gameSTARTchoice != "Y":
        time.sleep(1)
        gameSTARTchoice=input("Input here: ").upper()
        if gameSTARTchoice == "Y":
            print('Enjoy playing :)')
            gameplay()
            break
        else:   
            print("Invalid input. Please input Y to start.")

def rules(player_choice, opponent_choice):
    global player_score, opponent_score
    if player_choice == opponent_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and opponent_choice == "scissors"):
         print("You win this round!")
         player_score += 1
    elif (player_choice == "paper" and  opponent_choice == "rock"):
         print("You win this round!")
         player_score += 1
    elif (player_choice == "scissors" and opponent_choice == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print(" Your opponent wins this round.")
        opponent_score += 1
  
def gameplay():
    global opponent_score , player_score
    while True:
          player_choice = input("Enter rock, paper, or scissors: ").lower()
          opponent_choice = random.choice(options)
          print(f'You chose {player_choice}')
          time.sleep(1)
          print(f'opponent chose {opponent_choice}')
          
          if player_choice not in options:
            print("please enter rock, paper or scissors!!!")
            print("")
            continue
          
          rules(player_choice, opponent_choice)
          print(f'Player score  {player_score} | Opponent score {opponent_score}')
          
          if player_score >=10:
              print("You Won")
              break
          
          elif opponent_score >=10:
              print('Opponent Won')
              break

menu()

