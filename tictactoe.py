#! usr/bin/python3

import random

def display_board(board):
	sections = {'top': '{}||{}||{}', 'mid':'{}||{}||{}', 'bot':'{}||{}||{}', 'horizontal':'-------'}

	print(sections['top'].format(board[0], board[1], board[2])+'\n'+sections['horizontal']+'\n'+
		sections['mid'].format(board[3], board[4], board[5])+'\n'+sections['horizontal']+'\n'+
		sections['bot'].format(board[6], board[7], board[8]))

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
	#board.insert(position, marker)
	board[position] = marker
	return board

def win_check(board, mark):
	# 3 in horizontal, 2 in diagonal, 3 in vertical
	if (board[0] == board[1] == board[2] == mark) or (board[3] == board[4] == board[5]  == mark) or (board[6] == board[7] == board[8] == mark):
		return True
	elif (board[0] == board[4] == board[8] == mark) or (board[2] == board[4] == board[6] == mark):
		return True
	elif (board[0] == board[3] == board[6] == mark) or (board[1] == board[4] == board[7]  == mark) or (board[2] == board[5] == board[8] == mark):
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
	for i in range(0, 9):
		if space_check(board, i):
			return False
	return True

def player_choice(board,startPlayer):
	position = int(input(startPlayer + ' select board position (0 - 8): '))

	if space_check(board, position) == True:
		return position
	else:
		return ''

def replay():
	return input('Player again  (Y/N)').upper() == 'Y'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
	board = [' ']*9
	player1_marker, player2_marker = player_assign()
	startPlayer = choose_first()
	#startPlayer = 'Player 1'
	#print (startPlayer + ' goes first')
	game_on = True
	position = ''
	while game_on:
		if startPlayer == 'Player 1':
			while position == '':
				position = player_choice(board,startPlayer)
			player_input(board,player1_marker,position)
			display_board(board)
			if win_check(board,player1_marker) == True:
				#display_board(board)
				print(startPlayer + ' won!')
				game_on = False
				break
			elif full_board_check(board) == True:
				#display_board(board)
				print('Draw!')
				game_on = False
				break
			startPlayer = 'Player 2'
			# Reset position to allow for loop
			position = ''
		elif startPlayer == 'Player 2':
			while position == '':
				position = player_choice(board,startPlayer)
			player_input(board,player2_marker,position)
			display_board(board)
			if win_check(board,player2_marker) == True:
				#display_board(board)
				print(startPlayer + ' won!')
				game_on = False
				break
			elif full_board_check(board) == True:
				#display_board(board)
				print('Draw!')
				game_on = False
				break
			startPlayer = 'Player 1'
			# Reset position to allow for loop
			position = ''

	if replay() != True:
		break
