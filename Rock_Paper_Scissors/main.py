import random

# def play():
#     user = input("What's your choice 'r' rock, 'p' for paper, 's' for scissors: ")
#     computer = random.choice(['r', 'p', 's'])

#     if (user == computer):
#         print("It's Tie")
#     elif ((user == 'r' and computer == 's') or (user == 's' and computer == 'p') or \
#           (user == 'p' and computer == 'r')):
#         print("Hurray You've won")
#     else:
#         print("Sorry! You've lost")


# play()

# Better way of implementing
def play():
    user = input("What's your choice 'r' rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if(user == computer):
        return f"It's Tie, opponent also chose {computer}"
    
    if is_win(user, computer):
        return f"Hurray You've won, opponent chose {computer}"
    
    return f"Sorry! You've lost, opponent chose {computer}" 

def is_win(player, opponent):
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
          (player == 'p' and opponent == 'r')):
        return True
    
print(play())