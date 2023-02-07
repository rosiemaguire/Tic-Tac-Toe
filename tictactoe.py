# FUNCTIONS NEEDED FOR GAME
def display_board(board):
    print('\n'*100)
    middle = '---|---|---'
    upper = '   |   |  '
    lower = upper
    print(upper)
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print(lower)
    print(middle)
    print(upper)
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print(lower)
    print(middle)
    print(upper)
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])
    print(lower)


def player_input():
    marker = ''
    while marker not in ['X','O']:
        marker = input("Player 1: Do you want to be X or O? ").upper()
        
        if marker not in ['X','O']:
            print("Sorry, I don't understand, please choose X or O: ")
    player1 = marker
    
    if player1=='X':
        player2='O'
    else:
        player2='X'
    
    return(player1,player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return((board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[4]==mark and board[5]==mark and board[6]==mark) or
           (board[1]==mark and board[2]==mark and board[3]==mark) or
           (board[1]==mark and board[4]==mark and board[7]==mark) or
           (board[2]==mark and board[5]==mark and board[8]==mark) or
           (board[3]==mark and board[6]==mark and board[9]==mark) or
           (board[1]==mark and board[5]==mark and board[9]==mark) or
           (board[3]==mark and board[5]==mark and board[7]==mark) )

import random
def choose_first():
    if random.randint(1, 2) == 1:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for p in range(1,9):
        if space_check(board,p):
            return False
    return True

def player_choice(board):
    position = 0
    accept = list(range(1,10))

    while position not in accept or not space_check(board,position):
        try:
            position =int(input("Choose your next spot (1-9): "))
        except ValueError as e: 
                    print('Input an integer between 1 and 9!')
        if position not in accept or not space_check(board,position):
            print("Sorry, invalid choice!")               
    return position

def replay():
    return input("Do you want to play again? Enter 'Yes' or 'No' ").lower()[0]=='y'


# PUTTING THE GAME TOGETHER
print('Welcome to Tic Tac Toe!')

# WHLE LOOP TO KEEP RUNNING THE GAME
while True:
    
    # SET EVERYTHING UP (BOARD, WHO IS FIRST, CHOOSE MARKERS X,O ETC)
    myboard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    # GAME PLAY 
    play_game=input("Are you ready to play? Enter Yes or No. ")
    if play_game.lower()[0]=='y':
        game_on = True
    else:
        game_on = False
    
    # PLAYER ONE TURN
    while game_on:
        if turn == "Player 1":
            # Show the board
            display_board(myboard)
            # Print who's turn it is
            print("Player 1, it is your turn.")
            # Choose a position
            position = player_choice(myboard)
            # Place the marker on the position
            place_marker(myboard,player1_marker,position)
            
            # Check if they won
            if win_check(myboard,player1_marker):
                display_board(myboard)
                print("Congratulations, Player 1 has won!")
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("You have reached an impasse. This game is a draw!")
                    break
            # No tie and no win? Then next player's turn.
                else:
                    turn = "Player 2"
                    
                
                
        # PLAYER TWO TURN    
        else:
            # Show the board
            display_board(myboard)
            # Print who's turn it is
            print("Player 2, it is your turn.")
            # Choose a position
            position = player_choice(myboard)
            # Place the marker on the position
            place_marker(myboard,player2_marker,position)
            
            # Check if they won
            if win_check(myboard,player2_marker):
                display_board(myboard)
                print("Congratulations, Player 2 has won!")
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("You have reached an impasse. This game is a draw!")
                    break
            # No tie and no win? Then next player's turn.
                else:
                    turn = "Player 1"


    if not replay():
        break
    # BREAK OUT 9OF THE WHILE LOOP ON replay()