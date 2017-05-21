RANK=["a","b","c","d","e","f","g","h"]

def PrintBoard(board):
	return_board = ""
	for file in range(8):
		return_board += str(8-file)+" "
		for rank in range(8):
			return_board += "|"+board[7-file][rank]+"|"
		return_board += "\n"
	return_board += "    a   b   c   d   e   f   g   h"
	print return_board

def validMove(board,turn):
	if moveToCheck(board,turn):
		return True
	else:
		print "\nYou are in check please make another move\n"
		return False

def moveToCheck(board,turn):
	if turn == 0:
		for i in range(8):
			try:
				rank,file = board[i].index("Wk"),i
			except:
				pass

	for i in range(1,8):
		try:
			if board[file+i][rank] == "Br" or board[file+i][rank] == "Bq":
				return False
			elif board[file+i][rank] == "  ":
				pass
			else:
				break
		except:
			break

	return True



