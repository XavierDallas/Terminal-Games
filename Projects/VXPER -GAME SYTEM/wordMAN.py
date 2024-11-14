#XAVIER EDMOND

Life = 4
import time

print('Welcome to Word-Man')
time.sleep(1)
print('''The rules are simple.
      You have 4 four lives. For each answer wrong you lose a life.
      If you run out of lives it's a game-over 
       ''')
time.sleep(1)

print('Question 1')

while Life > 0:
     print('what swims the seven seas and has scales')
     ans = input('Enter answer: ').upper()
        
     if ans =='FISH':
          time.sleep(2)
          print('CORRECT!!!')
          break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')

print('Question 2')
while Life > 0:
     print('What is full of holes but still holds water?')
     ans = input('Enter answer: ').upper()
         #Question 2
     if ans =='SPONGE':
          time.sleep(2)
          print('CORRECT!!!')
          break
     if ans =='A SPONGE':
         time.sleep(2)
         print('CORRECT!!!')
         break
          

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')
   
print('Question 3') 
while Life > 0:
     print('What can you break, even if you never pick it up or touch it?')
     ans = input('Enter answer: ').upper()
     if ans =='A PROMISE':
           time.sleep(2)
           print('CORRECT!!!')
           break
     if ans =='PROMISE':
          time.sleep(2)
          print('CORRECT!!!')
          break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')
print("Question 4")
while Life > 0:
     print('The more of this there is, the less you see. What is it?')
     ans = input('Enter answer: ').upper()
     if ans =='THE DARKNESS':
           time.sleep(2)
           print('CORRECT!!!')
           break
     if ans =='DARKNESS':
          time.sleep(2)
          print('CORRECT!!!')
          break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')

print('Question 5')
while Life > 0:
     print(' What has many keys but can’t open a single lock?')
     ans = input('Enter answer: ').upper()
     if ans =='A PIANO':
           time.sleep(2)
           print('CORRECT!!!')
           break
     if ans =='PIANO':
          time.sleep(2)
          print('CORRECT!!!')
          break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')

print('Question 6')
while Life > 0:
     print("David's dad has three sons named, John, Danny and?")
     ans = input('Enter answer: ').upper()
     if ans =='DAVID':
           time.sleep(2)
           print('CORRECT!!!')
           break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')

print('Question 7')
while Life > 0:

     print("What year was the Emancipation Proclamation issued?")
     ans = (input('Enter answer: ')).upper()
     if ans =='1863':
           time.sleep(2)
           print('CORRECT!!!')
           break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')

print('Question 8')
while Life > 0:
     print('''Built for a king, my body guards him in death, not in life. 
           I stand tall, pointing to the skies, yet I am not alive. What am I?''')
     ans = input('Enter answer: ').upper()
     if ans =='PYRAMID':
           time.sleep(2)
           print('CORRECT!!!')
           break
     if ans=="A PYRAMID":
          time.sleep(2)
          print('CORECT!!!')
          break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')

print('Question 9')
while Life > 0:
     print(''' I make a loud sound when I’m changing. When I do change, 
           I get bigger but weigh less. What am I? ''')
     ans = input('Enter answer: ').upper()
     if ans =='POPCORN':
           time.sleep(2)
           print('CONGRATS!!!')
           break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')

print('Question 10')
while Life > 0:
     print("what is the chemistry formula for water")
     ans = input('Enter answer: ').upper()
     if ans =='H20':
           print('CORRECT!!!')
           break

     else:
       Life -= 1
     if Life > 0:
          print(f'Try again. {Life} lives remaining')
     else:
          print('Game Over')
          time.sleep(2)

if Life > 0:
     time.sleep(1)
     print('''CONGRATULATIONS, 
YOU'VE BECOME THE WORD KING.
THANK YOU FOR PLAYING''')


#bonus question
while Life>=4:
     print("SPECIAL BONUS ROUND!!!!")
     time.sleep(0.5)
     print('WHICH CAME FIRST? THE CHICKEN OR THE EGG')
     ans = input('Enter answer: ').upper()
     print('WHICH CAME FIRST? THE CHICKEN OR THE EGG')
    
     if ans == "EGG":
          print('CORRECT!!!')
          break

     else:
          print('Sadly No')
          break
     



     
