moveset1 = [(1,1),(1,-1),(-1,1),(-1,-1)]
moveset2 = [(0,1),(0,-1),(1,0),(-1,0)]
moveset3 = [(1,2),(-1,2),(2,1),(-2,1),(1,-2),(-1,-2),(2,-1),(-2,-1)]

def diag(row,col,start,len,board,iswhite):
    moves = []
    if (iswhite and board[row][col][0]!="W") or (not iswhite and board[row][col][0]!="B"):
        return []
    pos = (row,col)
    for move in moveset1:
        for x in range(start,len+start):
            r_move = row+x*move[0]
            c_move = col+x*move[1]
            pos2 = (r_move,c_move)
            if 0<=r_move<8 and 0<=c_move<8:
                if board[r_move][c_move]=="  ":
                    moves.append((pos,pos2))
                else:
                    if iswhite:
                        if board[r_move][c_move][0]=="B":
                            moves.append((pos,pos2))
                        if board[r_move][c_move][0]=="W":
                            
                            break
                    else:
                        if board[r_move][c_move][0]=="W":
                            moves.append((pos,pos2))
                        if board[r_move][c_move][0]=="B":
                            
                            break
                    break
            else:
                break
    return moves

def horivert(row,col,start,len,board,iswhite):
    moves = []
    if (iswhite and board[row][col][0]!="W") or (not iswhite and board[row][col][0]!="B"):
        return []
    pos = (row,col)
    for move in moveset2:
        for x in range(start,len+start):
            r_move = row+x*move[0]
            c_move = col+x*move[1]
            pos2 = (r_move,c_move)
            if 0<=r_move<8 and 0<=c_move<8:
                if board[r_move][c_move]=="  ":
                    moves.append((pos,pos2))
                else:
                    if iswhite:
                        if board[r_move][c_move][0]=="B":
                            moves.append((pos,pos2))
                        
                    else:
                        if board[r_move][c_move][0]=="W":
                            moves.append((pos,pos2))
                        
                    break
            else:
                break
    return moves

def lshape(row,col,board,iswhite):
    moves = []
    if (iswhite and board[row][col][0]!="W") or (not iswhite and board[row][col][0]!="B"):
        return []
    pos = (row,col)
    for move in moveset3:
        r_move = row+move[0]
        c_move = col+move[1]
        pos2 = (r_move,c_move)
        if 0<=r_move<8 and 0<=c_move<8:
            if board[r_move][c_move]=="  ":
                moves.append((pos,pos2))
            elif iswhite:
                if board[r_move][c_move][0]=="B":
                    moves.append((pos,pos2))
            else:
                if board[r_move][c_move][0]=="W":
                    moves.append((pos,pos2))
    return moves

def castle(board,state,iswhite):
    moves = []
    if not iswhite:
        if not state.BK_moved:
            if not state.lBR_moved and board[0][1]=="  " and board[0][2]=="  " and board[0][3]=="  ":
                pos1 = (0,4)
                pos2 = (0,0)
                moves.append((pos1,pos2))
            if not state.rBR_moved and board[0][6]=="  "and board[0][5]=="  ":
                pos1 = (0,4)
                pos2 = (0,7)
                moves.append((pos1,pos2))
    else:
        if not state.WK_moved:
            if not state.lWR_moved and board[7][1]=="  " and board[7][2]=="  " and board[7][3]=="  ":
                pos1 = (7,4)
                pos2 = (7,0)
                moves.append((pos1,pos2))
            if not state.rWR_moved and board[7][6]=="  "and board[7][5]=="  ":
                pos1 = (7,4)
                pos2 = (7,7)
                moves.append((pos1,pos2))
    return moves

def king_moves(row,col,board,iswhite):
    moves = []
    moves += diag(row,col,1,1,board,iswhite)
    moves += horivert(row,col,1,1,board,iswhite)
   # moves += castle(state.board,state,iswhite)
    return moves

def queen_moves(row,col,board,iswhite):
    moves = []
    moves+= diag(row,col,1,7,board,iswhite)
    moves+= horivert(row,col,1,7,board,iswhite)
    return moves

def bishop_moves(row,col,board,iswhite):
    moves = []
    moves+=diag(row,col,1,7,board,iswhite)
    return moves

def rook_moves(row,col,board,iswhite):
    moves = []
    moves+=horivert(row,col,1,7,board,iswhite)
    return moves

def knight_moves(row,col,board,iswhite):
    moves = []
    moves+=lshape(row,col,board,iswhite)
    return moves

def pawn_moves(row,col,board,iswhite):
    moves = []
    if (iswhite and board[row][col][0]!="W") or (not iswhite and board[row][col][0]!="B"):
        return []
    pos = (row,col)
    if iswhite:
        if row==6:
            if board[row-1][col]=="  ":
                moves.append((pos,(row-1,col)))
                if board[row-2][col]=="  ":
                    moves.append((pos,(row-2,col)))
            if col<7:
                if board[row-1][col+1][0]=="B":
                    moves.append((pos,(row-1,col+1)))
            if col>0:
                if board[row-1][col-1][0]=="B":
                    moves.append((pos,(row-1,col-1)))
        else:
            if row!=0:
                if board[row-1][col]=="  ":
                    moves.append((pos,(row-1,col)))
                if col<7:
                    if board[row-1][col+1][0]=="B":
                        moves.append((pos,(row-1,col+1)))
                if col>0:
                    if board[row-1][col-1][0]=="B":
                        moves.append((pos,(row-1,col-1)))
    else:
        if row==1:
            if board[row+1][col]=="  ":
                moves.append((pos,(row+1,col)))
                if board[row+2][col]=="  ":
                    moves.append((pos,(row+2,col)))
            if col<7:
                if board[row+1][col+1][0]=="W":
                    moves.append((pos,(row+1,col+1)))
            if col>0:
                if board[row+1][col-1][0]=="W":
                    moves.append((pos,(row+1,col-1)))
        else:
            if row!=7:
                if board[row+1][col]=="  ":
                    moves.append((pos,(row+1,col)))
                if col<7:
                    if board[row+1][col+1][0]=="W":
                        moves.append((pos,(row+1,col+1)))
                if col>0:
                    if board[row+1][col-1][0]=="W":
                        moves.append((pos,(row+1,col-1)))
    return moves
