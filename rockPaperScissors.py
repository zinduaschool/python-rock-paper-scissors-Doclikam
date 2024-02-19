# rock-paper-scissor game
import random


# assigning variables


player_score=0
cpu_score=0
round_count=0
tie_score=0
out_of_round= False


while round_count!=3:

    computer_hand=random.choice(('rock','paper','scissors'))

    player_hand=input("Enter a choice('rock','paper','scissors'): ").lower()


    def winner(player_hand, computer_hand):

        if (player_hand=='rock' and computer_hand=='paper'):

            print(f"you lose this round, {computer_hand} beats {player_hand}")

            winner= 'cpu'

        elif (player_hand=='rock' and computer_hand=='scissors'):

            print(f"you win this round, {player_hand} beats {computer_hand}")

            winner='player'

        elif (player_hand=='paper' and computer_hand=='scissors'):

            print(f"you lose this round, {computer_hand} beats {player_hand}")

            winner= 'cpu'

        elif (player_hand=='paper' and computer_hand=='rock'):

            print(f"you win this round, {player_hand} beats{computer_hand}")

            winner= 'player'

        elif (player_hand=='scissors' and computer_hand=='rock'):

            print(f"you lose this round, {computer_hand} beats {player_hand}")

            winner= 'cpu'

        elif (player_hand=='scissors' and computer_hand=='paper'):

            print(f"you win this round, {player_hand} beats {computer_hand}")

            winner='player'

        else:

            print(f"Its a tie, you picked {player_hand} and the cpu picked{computer_hand}")

            winner= 'tie'

        return winner

    round_count=round_count+1
    

    print(f"player: {player_hand}")

    print(f"computer: {computer_hand}")

    print(winner(player_hand, computer_hand))


while out_of_round:
    if winner=='player':
        player_score=player_score+1
        print(f"you score is {player_score}")  
        if player_score==2:
            print(f'you are the ultimate winner, your score is{player_score} ')
            break
    elif winner=='cpu':
        player_score=player_score+1
        if cpu_score==2:
            print(f'you lost you score is {player_score}')
            break
    else:
        tie_score=tie_score+1
        
        
    

    
        


    



 





