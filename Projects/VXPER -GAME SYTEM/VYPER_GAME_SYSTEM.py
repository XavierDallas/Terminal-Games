 # XAVIER EDMOND V00713888
import time
import random
gamecursor = ""
#menu
games = ["1", "2", "3", "4"]
print('WELCOME TO THE VXPER SYSTEM. PRESS ANYTHING TO CONTINUE')
time.sleep(1)
print(" ")
def menu():
    games = ["1", "2", "3", "4"]
    print('Please select a game from our selection')
    time.sleep(2)
    print('Game selection:')
    time.sleep(1)
    print("1- Word-MAN")
    time.sleep(1)
    print('2- NUMBER GUESSER')
    time.sleep(1)
    print('3- SNAKE EYES')
    time.sleep(1)
    print('4- Rock paper scissors')
    time.sleep(1)
    
    while True:
        try:
            gamecursor = (input('Enter the number of your selected game: '))
            
            if gamecursor in games:
                if gamecursor == "1":
                    print("You selected Word-MAN")
                    time.sleep(1)
                    print(" ")
                    print(" ")
                    wordgame()
                elif gamecursor == "2":
                    print("You selected Number Guesser")
                    print(" ")
                    print(" ")
                    time.sleep(1)
                    numbergame()
                elif gamecursor == "3":
                    print("You selected Snake Eyes")
                    print(" ")
                    print(" ")
                    time.sleep(1)
                    gamble()
                elif gamecursor == "4":
                    print("You selected Rock paper scissors")
                    print(" ")
                    print(" ")
                    time.sleep(1)
                    scissormenu()
                    
                
            else:
                print("Not available, please select a valid option")
        
        except ValueError:
            print("Invalid input, please enter a number from the game selection")

options = ["rock", "paper", "scissors"]
player_score = 0
opponent_score = 0
gameSTARTchoice =" "
player_choice = ""
opponent_choice = ""
#rock paper scisssors
def scissormenu():
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
def gameplay(player_choice, opponent_choice):
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
              player_score = 0
              opponent_score = 0
              menu()
              break
          
          elif opponent_score >=10:
              print('Opponent Won')
              player_score = 0
              opponent_score = 0
              menu()
              break
#============================================================================================================
#gamble game
def gamble():
    cash =int(100)
    D1 = random.randint(1,6)
    D2 =random.randint(1,6)
    print('WELCOME TO SNAKE EYES')
    print('THE GOAL OF THE GAME IS TO HAVE A BIGGER NUMBER THAN YOUR OPPONENT')
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
        print(" ")
        print("Opponent's turn.")
        time.sleep(2)
        print(f'Dice 1 rolled a {oD1}')
        time.sleep(2)
        print(f'Dice 2 rolled a {oD2}')
        time.sleep(2)
        print(f'Opponent dice value is {opponent_Dice}')
        print(" ")
        time.sleep(1)
        if opponent_Dice<User_dice:
            print('YOU WON')
            cash= cash+bet
        elif opponent_Dice>User_dice:
            cash= cash-bet
            print('You LOST')
        elif opponent_Dice==User_dice:
            cash= cash-bet
            print('DRAW')
            if cash<0:
                print('OUTTA CASH. MAYBE NEXT TIME')
                cash =int(100)
                menu()
                break
#============================================================================================================
#word Game
def wordgame():
    Life = 4
    print('Welcome to Word-Man')
    time.sleep(1)
    print('''The rules are simple.
      You have 4 lives. For each wrong answer, you lose a life.
      If you run out of lives, it's game over.
    ''')
    time.sleep(1)

    questions = [
        ("What swims the seven seas and has scales?", ["FISH"]),
        ("What is full of holes but still holds water?", ["SPONGE", "A SPONGE"]),
        ("What can you break, even if you never pick it up or touch it?", ["PROMISE", "A PROMISE"]),
        ("The more of this there is, the less you see. What is it?", ["DARKNESS", "THE DARKNESS"]),
        ('''What has many keys but can’t open a single lock?''', ["PIANO", "A PIANO"]),
        ("David's dad has three sons named, John, Danny and?", ["DAVID"]),
        ("What year was the Emancipation Proclamation issued?", ["1863"]),
        ("Built for a king, my body guards him in death, not in life. I stand tall, pointing to the skies, yet I am not alive. What am I?", ["PYRAMID", "A PYRAMID"]),
        ('''I make a loud sound when I’m changing. When I do change, I get bigger but weigh less. What am I?''', ["POPCORN"]),
        ("What is the chemistry formula for water?", ["H2O"])
    ]

    for i, (question, answers) in enumerate(questions, 1):
        print(f"Question {i}")
        while Life > 0:
            print(question)
            ans = input('Enter answer: ').upper()
            if ans in answers:
                time.sleep(1)
                print('CORRECT!!!')
                print(" ")
                break
            else:
                Life -= 1
                if Life > 0:
                    print(f'Try again. {Life} lives remaining')
                else:
                    print('Game Over')
                    print(" ")
                    menu()
                    return 

    if Life > 0:
        print("CONGRATULATIONS, YOU'VE BECOME THE WORD KING. THANK YOU FOR PLAYING!")

    # Bonus Question (only if player has all lives remaining)
    if Life == 4:
        print("SPECIAL BONUS ROUND!!!!")
        time.sleep(1)
        print("WHICH CAME FIRST? THE CHICKEN OR THE EGG?")
        ans = input("Enter answer: ").upper()
        if ans == "EGG":
            print("CORRECT!!!")
            menu()
        else:
            print("Sadly No")
            menu()
#=============================================================================================================
#Number Guesser
def numbergame():
    life = 10
    A = ""
    p = ""
    print("Welcome to Number Guesser!!!")
    time.sleep(2)
    print("To begin, please press P")
    
    while p != "P":
        p = input("Input P here: ").upper()
        if p != "P":
            print("Must press P to begin")
            print(" ")
    print(" ")
    time.sleep(1)
    print("Level 1 Begin")
    Num = random.randint(1, 5)
    while A != Num:
        print("Pick a number 1-5")
        time.sleep(1)
        A = int(input('Input answer here: '))
        if A == Num:
            print("CORRECT")
            time.sleep(1)
            print('Next Question')
        else:
            print("Wrong")
            life -= 1
            if life <= 0:
                print("Game Over")
                menu()
    
 
    print(" ")                
    Num = random.randint(1, 7)
    print("\nLevel 2 Begin")
    while A != Num:
        print("Pick a number 1-7")
        time.sleep(1)
        A = int(input('Input answer here: '))
        if A == Num:
            print("CORRECT")
            time.sleep(1)
            print('Next Question')
        else:
            print("Wrong")
            life -= 1
            if life <= 0:
                print("Game Over")
                menu()
    

    Num = random.randint(1, 9)
    print(" ")
                   
    print("Level 3 Begin")
    while A != Num:
        print("Pick a number 1-9")
        time.sleep(1)
        A = int(input('Input answer here: '))
        if A == Num:
            print("CORRECT")
            time.sleep(1)
            print('Next Question')
        else:
            print("Wrong")
            life -= 1
            if life <= 0:
                print("Game Over")
                menu()
    
    print(" ")
    Num = random.randint(1, 12)
    print("Level 4 Begin")
    while A != Num:
        print("Pick a number 1-12")
        time.sleep(1)
        A = int(input('Input answer here: '))
        if A == Num:
            print("CORRECT")
            time.sleep(1)
            print('Next Question')
        else:
            print("Wrong")
            life -= 1
            if life <= 0:
                print("Game Over")
                menu()
menu()

