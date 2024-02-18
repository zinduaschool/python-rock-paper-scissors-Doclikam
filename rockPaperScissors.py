#rock-paper-scissor game
import random

#assigning variables
options=('rock','paper','scissors')
computer_hand=random.choice(options)

player_hand=input('Enter a choice("rock","paper","scissors"): ')

print(f"player: {player_hand}")
print(f"computer: {computer_hand}")