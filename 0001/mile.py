def display_board(board):
	import os
	os.system('clear')
	
	print(board[7]+'|'+board[8]+'|'+board[9])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Takmicar 1: Da li zelite da budete X ili O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # gornja horiz. linija
    (board[4] == mark and board[5] == mark and board[6] == mark) or # srednja horiz. linija
    (board[1] == mark and board[2] == mark and board[3] == mark) or # donja horiz. linija
    (board[7] == mark and board[4] == mark and board[1] == mark) or # levo vertikalno
    (board[8] == mark and board[5] == mark and board[2] == mark) or # sredina vertikalno
    (board[9] == mark and board[6] == mark and board[3] == mark) or # desno vertiklano
    (board[7] == mark and board[5] == mark and board[3] == mark) or # dijagonala1
    (board[9] == mark and board[5] == mark and board[1] == mark)) # dijagonala2

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
	for i in range (1,10):
		if space_check(board,i):
			return False
	return True

def player_choice(board):
	pozicija = 0
	while pozicija not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pozicija):
		pozicija = int(input('Izaberite poziciju [1-9]: '))
	return pozicija

def replay():
	odgovor = input('Da li zelite ponovo da igrate [Da/Ne]: ')
	if odgovor.upper() == 'DA':
		return True
	else:
		return False

def igramo():
	odgovor = input('Da li zelite da igrate [Da/Ne]: ')
	if odgovor.upper() == 'DA':
		return True
	else:
		return False

print('dobrodosli u Iks&Oks')

while True:
	#prazna tabla
	tabla = [' ']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn+' pocinje prvi')

	da_li_igramo = igramo()

	while da_li_igramo:
		if turn == 'Player 1':
			#prikazi tablu
			display_board(tabla)
			#pitaj gde ce da igra
			position = player_choice(tabla)
			#postavi marker
			place_marker(tabla,player1_marker,position)

			#proveri da li je pobedio
			if win_check(tabla,player1_marker):
				display_board(tabla)
				print('Cestitam pobedili ste')
				da_li_igramo = False
			else:
				#proveri da li je tabla puna
				if full_board_check(tabla):
					display_board(tabla)
					print('Nereseno!')
					break
					#ili umesto break moze i da_li_igramo = False
				else:
					turn = 'Player 2'
		else:
			display_board(tabla)
			position = player_choice(tabla)
			place_marker(tabla,player2_marker,position)

			if win_check(tabla, player2_marker):
				display_board(tabla)
				print('Takmicar 2 je pobedio!')
				break
				#da_li_igramo = False
			else:
				if full_board_check(tabla):
					display_board(tabla)
					print('Nereseno!')
					break
				else:
					turn = 'Player 1'
	if not replay():
		break



empty_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
test_board = ['#','X','O','X','O','X','O','X','O','X']
#print(full_board_check(test_board))
#place_marker(empty_board,'$',8)
#display_board(empty_board)
#print(win_check(test_board,'X'))