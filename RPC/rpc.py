import random

def play():
    human = input('R for rock P for paper and S for scissors: ').lower()
    computer = random.choice(['r', 'p', 's'])

    if human == computer:
        return 'Tie'
    if is_win(human, computer):
        return 'You won'
    
    return 'You lost'


# logic 
# r > s / p > r / s > p
# 

def is_win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') \
        or (player1 == 's' and player2 == 'p'):
        return True

print(play())