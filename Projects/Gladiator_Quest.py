#Xavier Edmond
import time
import random
first_enemies= random.choice(['Bear', 'Lion', "Bull"])
second_enemies=random.choice(['Gladiator','Prisoner','Soldier'])
third_enemies=random.choice(['General', 'Captain','Commander'])
forth_enemies=random.choice(['Minotaur', 'Kraken','Seperpent'])
Final_enemies=random.choice(['King','Queen','Emperor'])
enemyNAMES=random.choice(['James','Williams','Crane','Andrews','Rainer','Dober'])
Secret_Boss="Cronus"
play =''
name = ""
hp = 100
en_hp = random.randint(90,130)
atk = random.randint(1,50)
bonus_atk= random.randint(1,2)
en_atk = random.randint(5,80)
defend =  30
choice = ""
damage_given = en_hp - atk
damage_taken = hp - en_atk
battle_choice=""

print("Welcome To Gladiator Quest!!!")
time.sleep(2)
print('To begin, please input press Y')
time.sleep(1)
while play != "Y":
    
    play = input('type Y here: ').upper()
    if play =="Y":
        print('Your Battles await')
        continue
    else:
        print('Must input Y to begin')
print("")   
while name =='':
     name= (input('What is your name?: '))
     if name=="":
         print('You must have a name Warrior')
         time.sleep(1)
     else:
         print('Peculiar name')

print('Entering the colosseum')
time.sleep(1)
print('An audience is roaring for entertainment')
time.sleep(1)
print("Across the from you a growl is heard")
print(f"A great {first_enemies} appears")
en_hp  = random.randint(80,110)
time.sleep(1)
print('PREPARE FOR BATTLE!!!')
print('''

''')
# Battle 1
while hp > 0 and en_hp > 0:
   

   
   
   print(f"Your HP: {hp}")
   print(f"Enemy HP: {en_hp}")

   print("Attack(A) Defend(D) ")
   atk = random.randint(6,70)
   en_atk = random.randint(1,50)
   choice = input("Attack (A) or Defend (D)? ").upper()
   time.sleep(1)
   if choice=="A":
    print(f'you did {atk} damage to the {first_enemies}')
    en_hp -= atk
    time.sleep(1)
   elif choice=="D":
    print("You chose to defend ")
    time.sleep(1)
    en_atk = max(en_atk - defend, 0) 
    print(f"You defended and reduced the {first_enemies}'s attack by {defend}.")
   else : print("Not an Option")
 
   if en_hp > 0:  
    print(f"The {first_enemies} dealt {en_atk} damage to you!")
    hp -= en_atk
   
   if hp <= 0:
      print("The story sadly ends here")
      exit()  

# reward 
print('Select A for Health or B for increased damage for your reward')
while battle_choice != 'A' and battle_choice != 'B':
    battle_choice = input('Input A or B: ').upper()

if battle_choice == "A":
    hp += 80
elif battle_choice == "B":
    bonus_atk += 20
else:
    print('Not an option')
    

time.sleep(1)
print('''

''')
#Battle 2
print('With the beast slain the crowd yells for your next opponent')
time.sleep(1)
print('walking out the dark entrance cackling is heard')
time.sleep(1)
print(f'YOUR NEXT BATTLE:{second_enemies} {enemyNAMES}!!')
en_hp =random.randint(100,120)
defend += 15

while hp > 0 and en_hp > 0:
 print(f"Your HP: {hp}")
 print(f"Enemy HP: {en_hp}")

 print("Attack(A) Defend(D) ")
 atk = random.randint(20,70)+ bonus_atk
 en_atk = random.randint(30,50)
 choice = input("Attack (A) or Defend (D)? ").upper()
 time.sleep(1)
 if choice=="A":
    print(f'you did {atk} damage to {second_enemies} {enemyNAMES}')
    en_hp -= atk
    time.sleep(1)
 elif choice=="D":
    print("You chose to defend ")
    time.sleep(1)
    en_atk = max(en_atk - defend, 0) 
    print(f"You defended and reduced the {second_enemies}'s attack by {defend}.")
 else : print("Not an Option")
 
 if en_hp > 0:  
    print(f"The {second_enemies} dealt {en_atk} damage to you!")
    hp -= en_atk
 
 if hp <= 0:
      print("The story sadly ends here")
      exit()  
     

time.sleep(1)
# reward 
battle_choice = "0"
print('Select A for Health or B for increased damage for your reward')
while battle_choice != 'A' and battle_choice != 'B':
    battle_choice = input('Input A or B: ').upper()

if battle_choice == "A":
    hp += 80
elif battle_choice == "B":
    bonus_atk += 20
else:
    print('Not an option')

time.sleep(1)

print('''

''')
# Battle 3
print(f''' "It seems that {name} has been on a streak". ''')
time.sleep(1)
print(''' "BRING EM OUT!!! " ''')
time.sleep(1)
print(f'A massive figure jumps out to you')
time.sleep(1)
print(f'A {forth_enemies} is infront of you!')
time.sleep(1)
print('PREPARE FOR BATTLE!!!!')
en_hp = int(150)
defend += 15

print('''

''')
while hp > 0 and en_hp > 0:
 print(f"Your HP: {hp}")
 print(f"Enemy HP: {en_hp}")

 print("Attack(A) Defend(D) ")
 atk = random.randint(20,70)+bonus_atk
 en_atk = random.randint(20,80)
 choice = input("Attack (A) or Defend (D)? ").upper()
 time.sleep(1)
 if choice=="A":
    print(f'you did {atk} damage to {forth_enemies} ')
    en_hp -= atk
    time.sleep(1)
 elif choice=="D":
    print("You chose to defend ")
    time.sleep(1)
    en_atk = max(en_atk - defend, 0) 
    print(f"You defended and reduced the {forth_enemies}'s attack by {defend}.")
 else : print("Not an Option")
 
 if en_hp > 0:  
    print(f"The {forth_enemies} dealt {en_atk} damage to you!")
    hp -= en_atk  

 if hp <= 0:
      print("The story sadly ends here")
      exit()  
time.sleep(1)
print('''

''')
battle_choice =""
print('Select A for Health or B for increased damage for your reward')
while battle_choice != 'A' and battle_choice != 'B':
    battle_choice = input('Input A or B: ').upper()
print('''

''')
if battle_choice == "A":
    hp += 120
elif battle_choice == "B":
    bonus_atk += 45
else:
    print('Not an option')
print('''

''')
time.sleep(1)

print(f'''As the dust settles 
the audience is speechless sees you still standing 
and {forth_enemies} on the ground lifeless''')
time.sleep(1)
defend += 15

#Battle 4
print(""" "You've bested our greatest warrior" someone in the crowd says. """)
time.sleep(1)
print(""" "It seems someone didn't get the memo to be a lamb"  """)
time.sleep(2)
print("  ")
print('A brawny figure drops down from the audience')
time.sleep(1)
print(""" "Your fame ends here " someone in the crowd says. """)
time.sleep(1)
print(f'I am {third_enemies} {enemyNAMES}')
defend += 15
en_hp = int(200)

while hp > 0 and en_hp > 0:
 print(f"Your HP: {hp}")
 print(f"Enemy HP: {en_hp}")

 print("Attack(A) Defend(D) ")
 atk = random.randint(18,100)+bonus_atk
 en_atk = random.randint(30,80)
 choice = input("Attack (A) or Defend (D)? ").upper()
 time.sleep(1)
 if choice=="A":
    print(f'you did {atk} damage to {third_enemies} {enemyNAMES}')
    en_hp -= atk + 7
    time.sleep(1)
 elif choice=="D":
    print("You chose to defend ")
    time.sleep(1)
    en_atk = max(en_atk - defend, 0) 
    print(f"You defended and reduced the {third_enemies}'s attack by {defend}.")
 else : print("Not an Option")
 
 if en_hp > 0:  
    print(f"The {third_enemies} dealt {en_atk} damage to you!")
    hp -= en_atk  

 if hp <= 0:
      print("The story sadly ends here")
      exit()  
time.sleep(1)

print('''

''')
battle_choice =""
print('Select A for Health or B for increased damage for your reward')
while battle_choice != 'A' and battle_choice != 'B':
    battle_choice = input('Input A or B: ').upper()

if battle_choice == "A":
    hp += 200
elif battle_choice == "B":
    bonus_atk += 38
else:
    print('Not an option')

time.sleep
print('''

''')
print(f'Congrats {name}')
print('''You've earned my respect.
      I give you the honor of being my right in conquering this world.
      ''')
time.sleep(1)
print('''"Will you take my offer?" ''')


print('')


en_hp = 300
while hp > 0 and en_hp > 0:
 print(f"Your HP: {hp}")
 print(f"Enemy HP: {en_hp}")

 print("Attack(A) Defend(D) ")
 atk = random.randint(25,99)+bonus_atk
 en_atk = random.randint(26,80)
 choice = input("Attack (A) or Defend (D)? ").upper()
 time.sleep(1)
 if choice=="A":
    print(f'you did {atk} damage to Cronus')
    en_hp -= atk
    time.sleep(1)
 elif choice=="D":
    print("You chose to defend ")
    time.sleep(1)
    en_atk = max(en_atk - defend, 0) 
    print(f"You defended and reduced the King Cronus's attack by {defend}.")
 else : print("Not an Option")
 
 if en_hp > 0:  
    print(f"The Kinng Cronus dealt {en_atk} damage to you!")
    hp -= en_atk  

 if hp <= 0:
      print(''' I wish you'd taken my offer.''')
      exit()  
      time.sleep(1)
      if en_hp <=0:
         print('*Cough* *Cough*')
         time.sleep(2)
         print(''' "I guess this is..... where my reign.....ends"''')
         time.sleep(2)
         print("")
         print("Having toppled all in the coliseum")
         time.sleep(2)
         print('')
         print(f'Emperor {name} now rules the lands')
         time.sleep(2)
print('''

''')
print('Thank you for playing!!!')
