RANK=["a","b","c","d","e","f","g","h"]
from utils import *
import copy

def whiteGetMove(board,move):
	rank = RANK.index(move[0])
	file = int(move[1])-1
	piece = board[file][rank]
	aMoves = []

	if piece == "Wp":
		try:
			if board[file+2][rank] == "  ":
				aMoves.append(RANK[rank]+str(file+2))
			if file == 1 and board[file+3][rank] == "  " and board[file+2][rank] == "  ": 
				aMoves.append(RANK[rank]+str(file+3))
			if "B" in board[file+1][rank+1]:
				aMoves.append(RANK[rank+1]+str(file+2))
			if "B" in board[file+1][rank-1]:
				aMoves.append(RANK[rank-1]+str(file+2))
		except:
			pass

	elif piece == "Wr":
		for i in range(1,8):
			try:
				if board[file+i][rank] == "  ":
					aMoves.append(RANK[rank]+str(file+i+1))
				elif "B" in board[file+i][rank]:
					aMoves.append(RANK[rank]+str(file+i+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank] == "  ":
						aMoves.append(RANK[rank]+str(file-i+1))
					elif "B" in board[file-i][rank]:
						aMoves.append(RANK[rank]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+1))
				elif "B" in board[file][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if rank-i >=0:
					if board[file][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+1))
					elif "B" in board[file][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+1))
						break
					else:
						break
				else:
					break
			except:
				break

	elif piece == "Wn":
		if file-2 >=0:
			if rank-1>=0:
				try:
					if board[file-2][rank-1] == "  " or "B" in board[file-2][rank-1]:
						aMoves.append(RANK[rank-1]+str(file-1))
				except:
					pass
			try:
				if board[file-2][rank+1] == "  " or "B" in board[file-2][rank+1]:
					aMoves.append(RANK[rank+1]+str(file-1))
			except:
				pass

		if file-1 >=0:
			if rank-2>=0:
				try:
					if board[file-1][rank-2] == "  " or "B" in board[file-1][rank-2]:
						aMoves.append(RANK[rank-2]+str(file))
				except:
					pass
			try:				
				if board[file-1][rank+2] == "  " or "B" in board[file-1][rank+2]:
					aMoves.append(RANK[rank+2]+str(file))
			except:
					pass		
		if rank-2>=0:
			try:
				if board[file+1][rank-2] == "  " or "B" in board[file+1][rank-2]:
					aMoves.append(RANK[rank-2]+str(file+2))
			except:
				pass		
		try:
			if board[file+1][rank+2] == "  " or "B" in board[file+1][rank+2]:
				aMoves.append(RANK[rank+2]+str(file+2))
		except:
			pass
		if rank-1>=0:
			try:
				if board[file+2][rank-1] == "  " or "B" in board[file+2][rank-1]:
					aMoves.append(RANK[rank-1]+str(file+3))
			except:
				pass
		try:
			if board[file+2][rank+1] == "  " or "B" in board[file+2][rank+1]:
				aMoves.append(RANK[rank+1]+str(file+3))
		except:
			pass
	
	elif piece == "Wq":
		for i in range(1,8):
			try:
				if board[file+i][rank] == "  ":
					aMoves.append(RANK[rank]+str(file+i+1))
				elif "B" in board[file+i][rank]:
					aMoves.append(RANK[rank]+str(file+i+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank] == "  ":
						aMoves.append(RANK[rank]+str(file-i+1))
					elif "B" in board[file-i][rank]:
						aMoves.append(RANK[rank]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+1))
				elif "B" in board[file][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if rank-i >=0:
					if board[file][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+1))
					elif "B" in board[file][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if rank-i >=-1:
					if board[file+i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+i+1))
					elif "B" in board[file+i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+i+1))
						break
					else:
						break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank+i] == "  ":
						aMoves.append(RANK[rank+i]+str(file-i+1))
					elif "B" in board[file-i][rank+i]:
						aMoves.append(RANK[rank+i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file+i][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+i+1))
				elif "B" in board[file+i][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+i+1))
					break
				else:
					break	
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0 and rank-i >=0:
					if board[file-i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file-i+1))
					elif "B" in board[file-i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		
	elif piece == "Wb":
		for i in range(1,8):
			try:
				if rank-i >=-1:
					if board[file+i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+i+1))
					elif "B" in board[file+i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+i+1))
						break
					else:
						break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank+i] == "  ":
						aMoves.append(RANK[rank+i]+str(file-i+1))
					elif "B" in board[file-i][rank+i]:
						aMoves.append(RANK[rank+i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file+i][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+i+1))
				elif "B" in board[file+i][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+i+1))
					break
				else:
					break	
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0 and rank-i >=0:
					if board[file-i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file-i+1))
					elif "B" in board[file-i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
	
	elif piece == "Wk":
		for x in [-1,0,1]:
			for y in [-1,0,1]:
				try:
					if board[file+x][rank+y] == "  " or "B" in board[file+x][rank+y]:
						if file+x>=0 and rank+y>=0:
							aMoves.append(RANK[rank+y]+str(file+1+x))
				except:
					pass
	
	return aMoves

def blackMove(board,move):
	rank = RANK.index(move[0])
	file = int(move[1])-1
	aMoves = []
	piece = board[file][rank]
	
	if piece == "Bp":
		try:
			if board[file-1][rank] == "  ":
				aMoves.append(RANK[rank]+str(file))
			if file == 6 and board[file-1][rank] == "  " and board[file-2][rank] == "  ": 
				aMoves.append(RANK[rank]+str(file-1))
			if "W" in board[file-1][rank+1]:
				aMoves.append(RANK[rank+1]+str(file))
			if "W" in board[file-1][rank-1]:
				aMoves.append(RANK[rank-1]+str(file))
		except:
			pass

	elif piece == "Br":
		for i in range(1,8):
			try:
				if board[file+i][rank] == "  ":
					aMoves.append(RANK[rank]+str(file+i+1))
				elif "W" in board[file+i][rank]:
					aMoves.append(RANK[rank]+str(file+i+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank] == "  ":
						aMoves.append(RANK[rank]+str(file-i+1))
					elif "W" in board[file-i][rank]:
						aMoves.append(RANK[rank]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+1))
				elif "W" in board[file][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if rank-i >=0:
					if board[file][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+1))
					elif "W" in board[file][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+1))
						break
					else:
						break
				else:
					break
			except:
				break

	elif piece == "Bn":
		if file-2 >=0:
			if rank-1>=0:
				try:
					if board[file-2][rank-1] == "  " or "W" in board[file-2][rank-1]:
						aMoves.append(RANK[rank-1]+str(file-1))
				except:
					pass
			try:
				if board[file-2][rank+1] == "  " or "W" in board[file-2][rank+1]:
					aMoves.append(RANK[rank+1]+str(file-1))
			except:
				pass

		if file-1 >=0:
			if rank-2>=0:
				try:
					if board[file-1][rank-2] == "  " or "W" in board[file-1][rank-2]:
						aMoves.append(RANK[rank-2]+str(file))
				except:
					pass
			try:				
				if board[file-1][rank+2] == "  " or "W" in board[file-1][rank+2]:
					aMoves.append(RANK[rank+2]+str(file))
			except:
					pass		
		if rank-2>=0:
			try:
				if board[file+1][rank-2] == "  " or "W" in board[file+1][rank-2]:
					aMoves.append(RANK[rank-2]+str(file+2))
			except:
				pass		
		try:
			if board[file+1][rank+2] == "  " or "W" in board[file+1][rank+2]:
				aMoves.append(RANK[rank+2]+str(file+2))
		except:
			pass
		if rank-1>=0:
			try:
				if board[file+2][rank-1] == "  " or "W" in board[file+2][rank-1]:
					aMoves.append(RANK[rank-1]+str(file+3))
			except:
				pass
		try:
			if board[file+2][rank+1] == "  " or "W" in board[file+2][rank+1]:
				aMoves.append(RANK[rank+1]+str(file+3))
		except:
			pass
	
	elif piece == "Bq":
		for i in range(1,8):
			try:
				if board[file+i][rank] == "  ":
					aMoves.append(RANK[rank]+str(file+i+1))
				elif "W" in board[file+i][rank]:
					aMoves.append(RANK[rank]+str(file+i+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank] == "  ":
						aMoves.append(RANK[rank]+str(file-i+1))
					elif "W" in board[file-i][rank]:
						aMoves.append(RANK[rank]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+1))
				elif "W" in board[file][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+1))
					break
				else:
					break
			except:
				break
		for i in range(1,8):
			 
			try:
				if rank-i >=0:
					if board[file][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+1))
					elif "W" in board[file][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if rank-i >=-1:
					if board[file+i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+i+1))
					elif "W" in board[file+i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+i+1))
						break
					else:
						break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank+i] == "  ":
						aMoves.append(RANK[rank+i]+str(file-i+1))
					elif "W" in board[file-i][rank+i]:
						aMoves.append(RANK[rank+i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file+i][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+i+1))
				elif "W" in board[file+i][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+i+1))
					break
				else:
					break	
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0 and rank-i >=0:
					if board[file-i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file-i+1))
					elif "W" in board[file-i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		
	elif piece == "Bb":
		for i in range(1,8):
			try:
				if rank-i >=-1:
					if board[file+i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file+i+1))
					elif "W" in board[file+i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file+i+1))
						break
					else:
						break
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0:
					if board[file-i][rank+i] == "  ":
						aMoves.append(RANK[rank+i]+str(file-i+1))
					elif "W" in board[file-i][rank+i]:
						aMoves.append(RANK[rank+i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
		for i in range(1,8):
			try:
				if board[file+i][rank+i] == "  ":
					aMoves.append(RANK[rank+i]+str(file+i+1))
				elif "W" in board[file+i][rank+i]:
					aMoves.append(RANK[rank+i]+str(file+i+1))
					break
				else:
					break	
			except:
				break
		for i in range(1,8):
			 
			try:
				if file-i >=0 and rank-i >=0:
					if board[file-i][rank-i] == "  ":
						aMoves.append(RANK[rank-i]+str(file-i+1))
					elif "W" in board[file-i][rank-i]:
						aMoves.append(RANK[rank-i]+str(file-i+1))
						break
					else:
						break
				else:
					break
			except:
				break
	
	elif piece == "Bk":
		for x in [-1,0,1]:
			for y in [-1,0,1]:
				try:
					if board[file+x][rank+y] == "  " or "W" in board[file+x][rank+y]:
						if file+x>=0 and rank+y>=0:
							aMoves.append(RANK[rank+y]+str(file+1+x))
				except:
					pass
	
	return aMoves

def displayMoves(moves):
	if len(moves)!=0:
		print "Avalible moves:"
		for i in range(len(moves)):
			print str(i+1)+". "+moves[i]
		#choice = raw_input("Select a move to make")
	else:
		print "Invalid move"

def movePieces(board,pos,move,turn):
	temp_board = copy.deepcopy(board)
	rank,file = RANK.index(move[0]), int(move[1])-1
	Prank,Pfile = RANK.index(pos[0]), int(pos[1])-1
	board[file][rank], board[Pfile][Prank] = board[Pfile][Prank], "  "
	if validMove(board,turn):
		turn+=1
		turn%=2
		return board,turn
		
	else:
		return temp_board, turn