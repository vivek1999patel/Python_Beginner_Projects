import random

def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Guess is larger than random number. Please try again!")
        elif guess < random_number:
            print("Guess is samller than random number. Please try again!")

    print(f"Hurray, you've guessed it correctly! {random_number}")
        
guess_number(5)