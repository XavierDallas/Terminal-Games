import random
import time

life = 10
A = ""
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

# Level 1
Num = random.randint(1, 5)
A = ""  # Reset A for new level
while A != Num:
    print("Pick a number 1-5")
    time.sleep(1)
    A = int(input('input answer here: '))
    if A == Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else:
        print("Wrong")
        life -= 1
        if life <= 0:
            print("Game Over")
            exit()

# Level 2
print("")
print("Level 2 Begin")
Num = random.randint(1, 7)
A = ""  # Reset A for new level
while A != Num:
    print("Pick a number 1-7")
    time.sleep(1)
    A = int(input('input answer here: '))
    if A == Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else:
        print("Wrong")
        life -= 1
        if life <= 0:
            print("Game Over")
            exit()

# Level 3
print("")
print("Level 3 Begin")
Num = random.randint(1, 9)
A = ""  # Reset A for new level
while A != Num:
    print("Pick a number 1-9")
    time.sleep(1)
    A = int(input('input answer here: '))
    if A == Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else:
        print("Wrong")
        life -= 1
        if life <= 0:
            print("Game Over")
            exit()

# Level 4
print("")
print("Level 4 Begin")
Num = random.randint(1, 12)
A = ""  # Reset A for new level
while A != Num:
    print("Pick a number 1-12")
    time.sleep(1)
    A = int(input('input answer here: '))
    if A == Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else:
        print("Wrong")
        life -= 1
        if life <= 0:
            print("Game Over")
            exit()

# Level 5
print("")
print("Level 5 Begin")
Num = random.randint(1, 15)
A = ""  # Reset A for new level
while A != Num:
    print("Pick a number 1-15")
    time.sleep(1)
    A = int(input('input answer here: '))
    if A == Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else:
        print("Wrong")
        life -= 1
        if life <= 0:
            print("Game Over")
            exit()

# Level 6
print("")
print("Level 6 Begin")
Num = random.randint(1, 20)
A = ""  # Reset A for new level
while A != Num:
    print("Pick a number 1-20")
    time.sleep(1)
    A = int(input('input answer here: '))
    if A == Num:
        print("CORRECT")
        time.sleep(1)
        print('Next Question')
    else:
        print("Wrong")
        life -= 1
        if life <= 0:
            print("Game Over")
            exit()

if life > 0:
    print("Congrats on beating Number Guesser!!")
