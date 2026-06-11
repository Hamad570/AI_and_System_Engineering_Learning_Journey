import random
number=random.randint(1,50)
while True:
    print("Guess a number between 1 to 50 I am guessing")
    guess=int(input("Enter number you guess: "))
    if guess>number:
        print("High")
    elif guess<number:
        print("Low")
    else: 
        print("Correct")
        break
