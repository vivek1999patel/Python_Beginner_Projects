import random

def play():
    user = ''
    computer = random.choice(["Apple", "Kiwi", "Grapes"]).lower()
    line = draw_lines(computer)
    points = 0

    while (''.join(line) != computer):
        if (points < 6):
            user = input("Guess the letter: ").lower()
            is_True, line = complete_puzzle(line, computer, user)
            print(line)
            if (is_True == False):
                points += 1
        elif(points == 6):
            print("You're hungman now!")
            break
    else:
        print("Hurray! You've guessed the correct word: ", computer)

def draw_lines(word):
    line = []
    for letter in range(0, len(word)):
        line.append("__")
    return line

def complete_puzzle(new_line, word, character):
    if (character in word):
        index = word.index(character)
        new_line[index] = character
        return True, new_line
    
    return False, new_line


play()