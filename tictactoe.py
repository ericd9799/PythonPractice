#! usr/bin/python3

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

display_board([' ']*10)
player1_marker, player2_marker = player_assign()

print(player1_marker)
print(player2_marker)
