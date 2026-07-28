#XAVIER EDMOND 

import random
import time 

def gamble():
    cash = int(100)
    print('WELCOME TO SNAKE EYES')
    print('THE GOAL OF THE GAME IS TO HAVE A BIGGER NUMBER THAN YOUR OPPONENT')
    
    while cash > 0:
        D1 = random.randint(1, 6)
        D2 = random.randint(1, 6)
        print(f''' 
        YOU HAVE ${cash}.
        WHEN READY INPUT THE MONEY TO BEGIN:''')
        
        try:
            bet = int(input('$'))
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if 1 <= bet <= cash:
            print(f'You bet ${bet}.')
            
            # Player's dice
            print(f'Dice 1 rolled a {D1}')
            time.sleep(2)
            print(f'Dice 2 rolled a {D2}')
            time.sleep(2)
            User_dice = D1 + D2
            print(f'Your dice value is {User_dice}')
            time.sleep(3)
            
            # Opponent's turn
            print("Opponent's turn.")
            time.sleep(2)
            oD1 = random.randint(1, 6)
            oD2 = random.randint(1, 6)
            print(f'Dice 1 rolled a {oD1}')
            time.sleep(2)
            print(f'Dice 2 rolled a {oD2}')
            time.sleep(2)
            opponent_Dice = oD1 + oD2
            print(f'Opponent dice value is {opponent_Dice}')
            time.sleep(1)
            
            # Determine winner
            if opponent_Dice < User_dice:
                print('YOU WON')
                cash = cash + bet
            elif opponent_Dice > User_dice:
                cash = cash - bet
                print('You LOST')
            elif opponent_Dice == User_dice:
                cash = cash - bet
                print('DRAW')
            
            print("")
            
            if cash <= 0:
                print('OUTTA CASH. MAYBE NEXT TIME')
                break
        else:
            print("Invalid bet. Please enter an amount between 1 and your current cash.")
    
    print(f"Final cash: ${cash}")

# Main game start
if __name__ == "__main__":
    gamble()
