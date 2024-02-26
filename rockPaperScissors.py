# rock-paper-scissor game
print('Hello.welcome to rock-paper-scissors.goodluck!')
print(' ')                                                             

#this module will select a random choice between rock paper and scissors
import random


# assigning variables
options=('rock','paper','scissors')
#keep track of the users wins
player_score=0
#keep track of the cpu wins
cpu_score=0
#keep track the number of rounds of the player. 
round_count=0


#loop runs when the round_count is less than 3.
while round_count!=3:

    computer_hand=random.choice(options)

    player_hand=input("Enter a choice('rock','paper','scissors'): ").lower()

    print(f"player: {player_hand}")

    print(f"computer: {computer_hand}")
    
    #after every round the round count increases to one, there are only three rounds.
    round_count=round_count+1
    #rules:rock beats scissors, scissors beats paper, paper beats rock.
    #when player does not insert rock,paper or scissors, they will be prompted to recheck their spelling
    if (player_hand not in options):
        print('invalid option, check spelling')

    elif (player_hand=='rock' and computer_hand=='paper'):

        print(f"you lose this round, {computer_hand} beats {player_hand}")

        cpu_score=cpu_score+1

    elif (player_hand=='rock' and computer_hand=='scissors'):

        print(f"you win this round, {player_hand} beats {computer_hand}")

        player_score=player_score+1

    elif (player_hand=='paper' and computer_hand=='scissors'):

        print(f"you lose this round, {computer_hand} beats {player_hand}")

        cpu_score=cpu_score+1

    elif (player_hand=='paper' and computer_hand=='rock'):

        print(f"you win this round, {player_hand} beats {computer_hand}")

        player_score=player_score+1

    elif (player_hand=='scissors' and computer_hand=='rock'):

        print(f"you lose this round, {computer_hand} beats {player_hand}")

        winner= 'cpu'
        
        cpu_score=cpu_score+1

    elif (player_hand=='scissors' and computer_hand=='paper'):

        print(f"you win this round, {player_hand} beats {computer_hand}")

        player_score=player_score+1
    else:

        print(f"Its a tie, you picked {player_hand} and the cpu picked {computer_hand}")
    
    print(f'ýour score is {player_score}')

#loop breaks if the player score or the computer is 2 and declares a winner. 
while player_score<3 and cpu_score<3:
    if (player_score==2):
        print('ýou are the ultimate winner:)!!')
        break
    #alternatively when the round count is three and player has less than a score of 2 the game ends
    if (round_count==3):
        print('computer won!!you are out of hands:(')
        break
