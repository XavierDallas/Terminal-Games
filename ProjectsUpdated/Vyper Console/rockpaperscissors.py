import random
import time

def rps_game():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    opponent_score = 0
    gameSTARTchoice = ""
    
    print("Welcome to Rock Paper Scissors:")
    time.sleep(1)
    print("To begin please input Y")
    time.sleep(1)
    
    while gameSTARTchoice != "Y":
        time.sleep(1)
        gameSTARTchoice = input("Input here: ").upper()
        if gameSTARTchoice == "Y":
            print('Enjoy playing :)')
            time.sleep(1)
            break
        else:
            print("Invalid input. Please input Y to start.")
    
    # Gameplay loop
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        
        if player_choice not in options:
            print("Please enter rock, paper or scissors!!!")
            print("")
            continue
        
        opponent_choice = random.choice(options)
        print(f'You chose {player_choice}')
        time.sleep(1)
        print(f'opponent chose {opponent_choice}')
        time.sleep(1)
        
        # Determine winner
        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and opponent_choice == "scissors"):
            print("You win this round!")
            player_score += 1
        elif (player_choice == "paper" and opponent_choice == "rock"):
            print("You win this round!")
            player_score += 1
        elif (player_choice == "scissors" and opponent_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Your opponent wins this round.")
            opponent_score += 1
        
        print(f'Player score: {player_score} | Opponent score: {opponent_score}')
        print("")
        
        if player_score >= 10:
            print("You Won!")
            break
        elif opponent_score >= 10:
            print('Opponent Won!')
            break
    
    return True

# Main game start
if __name__ == "__main__":
    rps_game()
