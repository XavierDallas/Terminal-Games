#XAVIER EDMOND

import time

def wordman_game():
    Life = 4
    
    print('Welcome to Word-Man')
    time.sleep(1)
    print('''The rules are simple.
    You have 4 lives. For each wrong answer you lose a life.
    If you run out of lives it's a game-over.
    ''')
    time.sleep(1)
    
    questions = [
        ("What swims the seven seas and has scales?", ["FISH"]),
        ("What is full of holes but still holds water?", ["SPONGE", "A SPONGE"]),
        ("What can you break, even if you never pick it up or touch it?", ["PROMISE", "A PROMISE"]),
        ("The more of this there is, the less you see. What is it?", ["DARKNESS", "THE DARKNESS"]),
        ("What has many keys but can't open a single lock?", ["PIANO", "A PIANO"]),
        ("David's dad has three sons named, John, Danny and?", ["DAVID"]),
        ("What year was the Emancipation Proclamation issued?", ["1863"]),
        ("Built for a king, my body guards him in death, not in life. I stand tall, pointing to the skies, yet I am not alive. What am I?", ["PYRAMID", "A PYRAMID"]),
        ("I make a loud sound when I'm changing. When I do change, I get bigger but weigh less. What am I?", ["POPCORN"]),
        ("What is the chemistry formula for water?", ["H2O", "H20"])
    ]
    
    for i, (question, answers) in enumerate(questions, 1):
        print(f"Question {i}")
        question_answered = False
        
        while Life > 0 and not question_answered:
            print(question)
            ans = input('Enter answer: ').upper()
            
            if ans in answers:
                time.sleep(1)
                print('CORRECT!!!')
                print("")
                question_answered = True
                break
            else:
                Life -= 1
                if Life > 0:
                    print(f'Try again. {Life} lives remaining')
                else:
                    print('Game Over')
                    print("")
                    return False
    
    if Life > 0:
        print("CONGRATULATIONS, YOU'VE BECOME THE WORD KING. THANK YOU FOR PLAYING!")
        print("")
        
        # Bonus question (only if player has all lives remaining)
        if Life == 4:
            print("SPECIAL BONUS ROUND!!!!")
            time.sleep(1)
            print("WHICH CAME FIRST? THE CHICKEN OR THE EGG?")
            ans = input("Enter answer: ").upper()
            if ans == "EGG":
                print("CORRECT!!!")
            else:
                print("Sadly No")
        
        return True
    
    return False

# Main game start
if __name__ == "__main__":
    wordman_game()
