#TicTacToe Game
from IPython.display import clear_output
import random

#draw 3 x 3 table
def display_board(board):
    clear_output()
    print (board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('--+---+--')
    print (board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('--+---+--')
    print (board[1] + ' | ' + board[2] + ' | ' + board[3])
board  = ['']*10
#display_board(board)

#Player chooses their character X or O
def player_assign_character():
	player_choice = ''
	while player_choice != 'X' and player_choice != 'O':
		player_choice = input('1st Player please choose either "X" or "O": ').upper()
	#Assign player 2, opposite choice player1 = player_choice
	player1 = player_choice
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return (player1,player2)

#Select who goes first with coin flip 
#use a coin flip function from random
def whoGoesFirst():
	if random.randint(0,1) == 0:
		return 'Player 1 goes first'
	else:
		return 'Player 2 goes first'

#Placing the X or O onto the board's position. 
#Place the POSITION of the POINT X || O onto the BOARD
def place_marker_on_board(board,marker,position):
    board[position] = marker

# Check function to see if position on board is free
def position_space_check(board,position):
    return board[position] == ''

# check if the board is full 
def board_is_full_check(board):
    for space in range (1,10):
        if space == '':
            return True
    return False

# ask for player's next move by asking them to choose 1-9 
# check if position if free
def player_move(board):
    move = 0
    while move not in [1,2,3,4,5,6,7,8,9] or not position_space_check(board,move):
        move = int(input('Choose you move for next position from : 1 to 9 '))
    return move

#Check if position placed wins the game
def winning_check(board,marker):
	return( (board[7] == marker and board[8] == marker and board[9] == marker) or
		(board[4] == marker and board[5] == marker and board[6] == marker) or
		(board[1] == marker and board[2] == marker and board[3] == marker) or
		(board[1] == marker and board[5] == marker and board[3] == marker) or
		(board[3] == marker and board[5] == marker and board[7] == marker) or
		(board[1] == marker and board[4] == marker and board[7] == marker) or
		(board[2] == marker and board[5] == marker and board[8] == marker) or
		(board[3] == marker and board[6] == marker and board[9] == marker) )

#asking player to play again
def playAgain():
	print('Do you want to play again? ( Yes or No )')
	return input('').lower().startswith('y')

# START OF THE PROGRAM

print ('------- W E L C O M E     T O     T I C  . T A C . T O E -------')

while True:
	# Show the board & clear board
	board  = ['']*10
	#Assign Character to player 1
	player1,player2 = player_assign_character()
	# Select who goes first
	turn = whoGoesFirst()
	# Track game is on or off 
	game_tracker = input('Are you ready to start the game? ( Yes or No ): ').lower()
	if game_tracker.lower()[0] == 'y':
		game_tracker = True
	else:
		game_tracker = False

	while game_tracker:
		if turn == 'Player 1 goes first':
			display_board(board)

			# Player 1 makes move
			position = player_move(board)
			
			# Update the board
			place_marker_on_board(board,player1,position)

			# Check if win
			if winning_check(board,player1):
				display_board(board)
				print('Congratulations!!! You have won the game!')
				game_tracker = False
			else:
				if board_is_full_check(board):
					display_board(board)
					print('It is a tie!')
					break
				else:
					turn = 'Player 2 goes first '
		else:
			display_board(board)
			position1 = player_move(board)
			place_marker_on_board(board, player2, position1)
			if winning_check(board,player2):
				display_board(board)
				print('Congratulations!!! You have won the game!')
			else:
				if board_is_full_check(board):
					display_board(board)
					print('It is a tie!')
					break
				else:
					turn = "Player 1 goes first"
	if not playAgain():
		break


