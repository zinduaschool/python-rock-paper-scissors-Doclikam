# rock-paper-scissor game
import random

# assigning variables
options=('rock','paper','scissors')

player_score=0
cpu_score=0
round_count=0

# function to compare the player hand and computer hand in each round
def hand_wins(player_hand, computer_hand):
    # rock>scissors, scissors>paper, paper>rock
    if player_hand==computer_hand:
        print(f"Its a tie, you picked {player hand} and the cpu picked{computer_hand}")
        return 'tie'
    elif player_hand='rock' and computer_hand='paper':
        print(f"you lose, {computer_hand} beats{player_hand}")
        return 'cpu'
    elif player_hand='rock' and computer_hand='scissors':
        print(f"you win, {player_hand} beats{computer_hand}")
        return 'player'
    elif player_hand='paper' and computer_hand='scissors':
        print(f"you lose, {computer_hand} beats{player_hand}")
        return 'cpu'
    elif player_hand='paper' and computer_hand='rock':
        print(f"you win, {player_hand} beats{computer_hand}")
        return 'player'
    elif player_hand='scissors' and computer_hand='rock':
        print(f"you lose, {computer_hand} beats{player_hand}")
        return 'cpu'
    elif player_hand='scissors' and computer_hand='paper':
        print(f"you win, {player_hand} beats{computer_hand}")
        return 'player'
    else:
        print("invalid input,check your spelling")







computer_hand=random.choice(options)

player_hand=input('Enter a choice("rock","paper","scissors"): ')

print(f"player: {player_hand}")
print(f"computer: {computer_hand}")