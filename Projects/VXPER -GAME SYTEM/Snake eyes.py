#XAVIER EDMOND 

import random
import time 
cash =int(100)
D1 = random.randint(1,6)
D2 =random.randint(1,6)
print('WELCOME TO SNAKE EYES')
print('THE GOAL OF THE GAME IS TO HAVE A BIGGER NUMBER THAN YOUR OPPONENT')

def gamble():
   while cash > 0:
     D1 = random.randint(1,6)
     D2 =random.randint(1,6)
     print(F''' 
           YOU HAVE ${cash}.
             WHEN READY INPUT THE MONEY TO BEGIN:''')
     bet = int(input('$')) 
     #bet = int(input('$'))
     if 1 <= bet <= cash:
        print(f'You bet ${bet}.')
        #opponent dice
        oD1 = random.randint(1,6)
        oD2 =random.randint(1,6)
        opponent_Dice = oD1+oD2
        print(f'Dice 1 rolled a {D1}')
        time.sleep(2)
        print(f'Dice 2 rolled a {D2}')
        time.sleep(2)
        User_dice = D1 + D2
        print(f'Your dice value is {User_dice}')
        time.sleep(3)
        print("Opponent's turn.")
        time.sleep(2)
        print(f'Dice 1 rolled a {oD1}')
        time.sleep(2)
        print(f'Dice 2 rolled a {oD2}')
        time.sleep(2)
        print(f'Opponent dice value is {opponent_Dice}')
        time.sleep(1)
        if opponent_Dice<User_dice:
            print('YOU WON')
            cash= cash+bet
        elif opponent_Dice>User_dice:
            cash= cash-bet
            print('You LOST')
        elif opponent_Dice==User_dice:
            cash= cash-bet
            ('DRAW')
            if cash<0:
                print('OUTTA CASH. MAYBE NEXT TIME')
                



    

        
        
    
    

    
