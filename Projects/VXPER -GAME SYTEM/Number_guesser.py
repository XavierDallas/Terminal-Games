import random
import time

life= 10
Num = random.randint(1,5)
A=""
p = ""
print("Welcome to Number Guesser!!!")
time.sleep(2)
print("to begin please press P")
while p != "P":
    
    p = input("input P here: ").upper()
    if p == "P":
        "Start"
    else:
        print("Must press P to begin")

time.sleep(1)
print("")
print("Level 1 Begin")
while  A!= Num:
    print("Pick a number 1-5")
    time.sleep(1)
    A=int(input('input answer here: '))
    if A== Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else: print("Wrong")
    life-=1
    if life <=0:
        print("Game Over")
        exit()
Num = random.randint(1,7)
print("")
print("Level 2 Begin")
while  A!= Num:
    print("Pick a number 1-7")
    time.sleep(1)
    A=int(input('input answer here: '))
    if A== Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else: print("Wrong")
    life-=1
    if life <=0:
        print("Game Over")
        exit()

Num = random.randint(1,9)
print("")
print("Level 3 Begin")
while  A!= Num:
    print("Pick a number 1-9")
    time.sleep(1)
    A=int(input('input answer here: '))
    if A== Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else: print("Wrong")
    life-=1
    if life <=0:
        print("Game Over")
        exit()

Num = random.randint(1,12)
print("")
print("Level 4 Begin")
while  A!= Num:
    print("Pick a number 1-12")
    time.sleep(1)
    A=int(input('input answer here: '))
    if A== Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else: print("Wrong")
    life-=1
    if life <=0:
        print("Game Over")
        exit()

Num = random.randint(1,15)
print("")
print("Level 5 Begin")
while  A!= Num:
    print("Pick a number 1-15")
    time.sleep(1)
    A=int(input('input answer here: '))
    if A== Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else: print("Wrong")
    life-=1
    if life <=0:
        print("Game Over")
        exit()
Num = random.randint(1,20)
print("")
print("Level 6 Begin")
while  A!= Num:
    print("Pick a number 1-20")
    time.sleep(1)
    A=int(input('input answer here: '))
    if A== Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else: print("Wrong")
    life-=1
    if life <=0:
        print("Game Over")
        exit()

if life >0:
    print("Congrats on beating Number Guesser!!")
