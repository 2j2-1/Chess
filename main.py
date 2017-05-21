#Chess
from utils import *
from movement import *
from attack import *
import copy

STARTINGBOARD =[["Wr","Wn","Wb","Wq","Wk","Wb","Wn","Wr"],
				["Wp","Wp","Wp","Wp","Wp","Wp","Wp","Wp"],
				["  ","  ","  ","  ","  ","  ","  ","  "],
				["  ","  ","  ","  ","  ","  ","  ","  "],
				["  ","  ","  ","  ","  ","  ","  ","  "],
				["  ","  ","  ","  ","  ","  ","  ","  "],
				["Bp","Bp","Bp","Bp","Bq","Bp","Bp","Bp"],
				["Br","Bn","Bb","Bq","Bk","Bb","Bn","Br"]]

RANK=["a","b","c","d","e","f","g","h"]
players = ["White's", "Black's"]
computers_turn = 2
playerTurn = 0
def main(board):
	while 1:
		print players[playerTurn] + " turn please chose a piece to move\n"
		PrintBoard(board)
		moveString = raw_input()
		board = move(board, moveString, playerTurn)
	

def move(board,move,turn):
	aMoves = []
	global playerTurn
	if turn == 0:
			aMoves = whiteGetMove(board,move)
	else:
			aMoves = blackMove(board,move)

	if turn == computers_turn:
		for i in aMoves:
			PrintBoard(movePieces(copy.deepcopy(board),move,i,turn))
	else:
		print
		displayMoves(aMoves)
		board,playerTurn = movePieces(copy.deepcopy(board),move,aMoves[input("Choose a move ")-1],turn)
	return board
	
main(STARTINGBOARD)