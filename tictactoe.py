#! usr/bin/python3

import random

def display_board(board):
	sections = {'top': '{}||{}||{}', 'mid':'{}||{}||{}', 'bot':'{}||{}||{}', 'horizontal':'-------'}

	print(sections['top'].format(board[1], board[2], board[3])+'\n'+sections['horizontal']+'\n'+
		sections['mid'].format(board[4], board[5], board[6])+'\n'+sections['horizontal']+'\n'+
		sections['bot'].format(board[7], board[8], board[9]))

def player_assign():
	marker = ''

	while marker != 'X' and  marker != 'O':
		marker = input('Player 1 enter X or O: ')
	
	player1 = marker

	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

	return(player1, player2)

def player_input(board,marker,position):
	
	#position = int(input('Player {} selection board position (1 - 9): '.format(player)))
	board.insert(position, marker)
	return board

def win_check(board, mark):
	# 3 in horizontal, 3 in diagonal, 3 in vertical
	if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6]  == mark) or (board[7] == board[8] == board[9] == mark):
		return True
	elif (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
		return True
	elif (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8]  == mark) or (board[3] == board[6] == board[9] == mark):
		return True
	else:
		return False

def choose_first():
	if random.randint(0,1) == 1:
		return 'Player 1'
	else:
		return 'Player 2'
	
def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
	for i in range(1, 10):
		if space_check(board, i):
			return False
	return True

def player_choice(board):
	position = int(input('Select board position (1 - 9): '))
	if space_check(board, position):
		return position
	
def replay():
	return input('Player again  (Y/N)').upper() == 'Y'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
	board = [' ']*10
	player1_marker, player2_marker = player_assign()
	#startPlayer = choose_first()
	startPlayer = 'Player 1'
	print (startPlayer + ' goes first')
	game_on = True

	while game_on:
		if startPlayer == 'Player 1':	
			display_board(board)
			position = player_choice(board)
			player_input(board,player1_marker,position)
			if win_check(board,player1_marker) == True:
				display_board(board)
				print(startPlayer + ' won!')
				game_on = False
				break
			startPlayer = 'Player 2'
		elif startPlayer == 'Player 2':
			display_board(board)
			position = player_choice(board)
			player_input(board,player2_marker,position)
			if win_check(board,player2_marker) == True:
				display_board(board)
				print(startPlayer + ' won!')
				game_on = False
				break
			startPlayer = 'Player 1'

	if replay() != True:
		break			
