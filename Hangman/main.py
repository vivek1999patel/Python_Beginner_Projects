import random

def play():
    user = ''
    computer = random.choice(["Apple", "Kiwi", "Grapes"]).lower()
    line = draw_lines(computer)
    used_letters = set()
    print(line)
    points = 0

    while (''.join(line) != computer):
        if (points < 6):
            user = input("Guess the letter: ").lower()
            used_letters.add(user)
            if(user in computer):
                line = complete_puzzle(line, computer, used_letters)
                print("User letters: ", used_letters)
                print(line)
            else:
                print("User letters: ", used_letters)
                print(line)
                points += 1
        elif(points == 6):
            print("You're hungman now!")
            break
    else:
        print("Hurray! You've guessed the correct word: ", computer)

def draw_lines(word):
    line = []
    for letter in range(0, len(word)):
        line.append("-")
    return line

def complete_puzzle(line, word, used_letters):
    # word_list = [letter if letter in used_letters else '-' for letter in word]
    # Above is better way
    word_list = line
    for index,letter in enumerate(word):
        if (letter in used_letters):
            word_list[index] = letter
        else:
            word_list[index] = '-'
    
    return word_list

play()