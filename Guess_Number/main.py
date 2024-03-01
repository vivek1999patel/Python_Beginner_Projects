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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} is too low (L), or too high (H), or correct (C) : ").lower()
        if feedback == "H":
            high = guess - 1
            print("It's too High")
        elif feedback == "L":
            low = guess + 1
            print("It's too Low")

    print(f"Hurray, you guess the correct number {guess}")
        
# guess_number(5)
computer_guess(5)