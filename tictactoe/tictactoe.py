# Tic Tac Toe Game Using CLI and ASCII
import os
from random import randint
from time import sleep


player_board = [" " for _ in range(9)]
legend_board = [str(i) for i in range(1,10)]


def print_game_board(player_board):
    """Function Prints ASCII Game Board"""
    pb = player_board
    lb = legend_board
    row_1 =  pb[0] + '|' + pb[1] + '|' + pb[2] + "    " +  lb[0] + '|' + lb[1] + '|' + lb[2]
    row_2 = pb[3] +'|' + pb[4] + '|' + pb[5] + "    " +  lb[3] + '|' + lb[4] + '|' + lb[5]
    row_3 = pb[6] + '|' + pb[7] + '|' + pb[8] + "    " +  lb[6] + '|' + lb[7] + '|' + lb[8]

    print(row_1)
    print("_ " * 3)
    print(row_2)
    print("_ " * 3)
    print(row_3)



def valid_space(number):
    # Function returns true if number space is free
    return player_board[number - 1] == ' '


def check_winner(pb, turn):
    """Function checks to see if user won the game"""

    # created list with each possible win as a list
    row_winners = [pb[:3], pb[3:6], pb[6:]]
    col_winners = [
        [pb[0], pb[3], pb[6]],
        [pb[1], pb[4], pb[7]],
        [pb[2], pb[5], pb[8]],
    ]
    diag_winners = [
        [pb[0], pb[4], pb[8]],
        [pb[6], pb[4], pb[2]],
    ]

    # Loop to check winner
    for item in row_winners:
        if all(turn == i[0] for i in item):
            return True
    for item in col_winners:
        if all(turn == i[0] for i in item):
            return True
    for item in diag_winners:
        if all(turn == i[0] for i in item):
            return True
    
    return False


def game():
    """Main game Function"""
    global player_board
    game_on = True

    turn = 'X'
    count = 0


    while game_on:

        os.system('clear')
        print('Tic Tac Toe:\n        Legend:')
        print_game_board(player_board)
        print(" ")


        player_choice = int(input('Choose a number for where to place an X: \n'))
        turn = 'X'

        while not valid_space(player_choice):
            print('Space Taken. Enter New Number')
            sleep(1)
            player_choice = int(input('Choose a number for where to place an X: \n'))
        else:
            player_board[player_choice - 1] = 'X'

            
            
            if check_winner(player_board, turn):
                game_on = False

            # let random choose a random spot to place the O (computer)
            computer_choice = randint(1,9)
            
            # randomly picks cpu move and checks if cpu won
            while not valid_space(computer_choice) and game_on:
                computer_choice = randint(1,9)
            else:
                # Checks to see if game is won by X if not plays computers move
                if game_on:
                    player_board[computer_choice - 1] = 'O'
                    turn = 'O'
                    # check if computer one game
                    if check_winner(player_board, turn):
                        game_on = False
                


        count += 1

        # Basically game ended in a tie
        if count == 9 and game_on:
            game_on = False
            turn = 'Tie'

        # Print winning message and prompt to play again
        if game_on == False:
            os.system('clear')
            print(f'{turn} took the game')
            print_game_board(player_board)

            play_again = input('Play again? Y or N\n').lower()
            if play_again == 'y':
                # Reset Player Board and load the new game
                player_board = [" " for _ in range(9)]
                game()

if __name__ == '__main__':
    game()




    