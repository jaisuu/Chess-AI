import moves,random
HIGH = 130
DEPTH = 3
points = {"P":1,"N":3,"B":3,"R":5,"Q":9,"K":90," ":0}
def eval(board):
    score = 0
    for r in range(0,8):
       for c in range(0,8):
           if board[r][c][0]=="W":
               score+=points[board[r][c][1]]
           else:
               score-=points[board[r][c][1]]
    return score
def in_check(board,r,c,iswhite):
    moveset1 = moves.moveset1
    moveset2 = moves.moveset2
    moveset3 = moves.moveset3
    pos = (r,c)
    for move in moveset1:
        for x in range(1,8):
            r_move = r+x*move[0]
            c_move = c+x*move[1]
            pos2 = r_move,c_move
            if 0<=r_move<8 and 0<=c_move<8:
                if iswhite:
                    if board[r_move][c_move]=="BQ" or board[r_move][c_move]=="BB":
                        return True
                    elif board[r_move][c_move]!="  ":
                        break
                else:
                    if board[r_move][c_move]=="WQ" or board[r_move][c_move]=="WB":
                        return True
                    elif board[r_move][c_move]!="  ":
                        break
            else:
                break

    for move in moveset2:
        for x in range(1,8):
            r_move = r+x*move[0]
            c_move = c+x*move[1]
            pos2 = r_move,c_move
            if 0<=r_move<8 and 0<=c_move<8:
                if iswhite:
                    if board[r_move][c_move]=="BQ" or board[r_move][c_move]=="BR":
                        return True
                    elif board[r_move][c_move]!="  ":
                        break
                else:
                    if board[r_move][c_move]=="WQ" or board[r_move][c_move]=="WR":
                        return True
                    elif board[r_move][c_move]!="  ":
                        break
            else:
                break
    for move in moveset3:
        r_move = r+move[0]
        c_move = c+move[1]
        if 0<=r_move<8 and 0<=c_move<8:
            if iswhite:
                if board[r_move][c_move]=="BN":
                    return True
            else:
                if board[r_move][c_move]=="WN":
                    return True
    if iswhite:
        if r+1<8 and c-1>=0:
            if board[r+1][c-1]=="BP" or board[r+1][c-1]=="BK":
                return True
        if r+1<8 and c+1<8:
            if board[r+1][c+1]=="BP" or board[r+1][c+1]=="BK":
                return True
    else:
        if r-1>=0 and c-1>=0:
            if board[r-1][c-1]=="WP" or board[r-1][c-1]=="WK":
                return True
        if r-1>=0 and c+1<8:
            if board[r-1][c+1]=="WP" or board[r-1][c+1]=="WK":
                return True
    return False
def get_moves(board,iswhite):
    move_set = []
    for r in range(0,8):
        for c in range(0,8):
            if (board[r][c][0]=="W" and iswhite) or (board[r][c][0]=="B" and not iswhite):
                if board[r][c][1]=="P":
                    move_set+=(moves.pawn_moves(r,c,board,iswhite))
                if board[r][c][1]=="K":
                    move_set+=(moves.king_moves(r,c,board,iswhite))
                if board[r][c][1]=="Q":
                    move_set+=(moves.queen_moves(r,c,board,iswhite))
                if board[r][c][1]=="B":
                    move_set+=(moves.bishop_moves(r,c,board,iswhite))
                if board[r][c][1]=="N":
                    move_set+=(moves.knight_moves(r,c,board,iswhite))
                if board[r][c][1]=="R":
                    move_set+=(moves.rook_moves(r,c,board,iswhite))
    illegal_moves = []
    WK = None
    BK = None
    for r in range(0,8):
        for c in range(0,8):
            if board[r][c]=="WK":
                WK = (r,c)
            if board[r][c]=="BK":
                BK = (r,c)
            if WK!=None and BK!=None:
                break
        if WK!=None and BK!=None:
                break
    """
    for x in range(len(move_set)):
        move = move_set[x]
        piece1 = board[move[0][0]][move[0][1]]
        piece2 = board[move[1][0]][move[1][1]]
        board[move[0][0]][move[0][1]] = "  "
        board[move[1][0]][move[1][1]] = piece1
        if iswhite:
            if in_check(board,WK[0],WK[1],True):
                illegal_moves.append(x)
        else:
            if in_check(board,BK[0],BK[1],False):
                illegal_moves.append(x)
        board[move[0][0]][move[0][1]] = piece1
        board[move[1][0]][move[1][1]] = piece2
    illegal_moves.reverse()
    for x in illegal_moves:
        move_set.pop(x)
    """
    return move_set
def random_move(board,iswhite):
    move_set = get_moves(board,iswhite)
    if len(move_set)==0:
        return None
    return move_set[random.randrange(len(move_set))]
def minimax_move(board,iswhite,depth):
    curr_score = eval(board)
    best_moves = minimax(board,iswhite,depth,-HIGH,HIGH,1 if iswhite else -1)[0]
    if len(best_moves)==0:
        return None
    return best_moves[random.randrange(len(best_moves))]


def minimax(board,iswhite,depth,alpha,beta,neg):

    move_set = get_moves(board,iswhite)
    if depth==0:
        return [],eval(board)
    if depth==DEPTH:
        best_move = []
    if iswhite:
        best_score = -HIGH
    else:
        best_score = HIGH
    for move in move_set:
        piece1 = board[move[0][0]][move[0][1]]
        piece2 = board[move[1][0]][move[1][1]]
        board[move[0][0]][move[0][1]] = "  "
        board[move[1][0]][move[1][1]] = piece1
        score = minimax(board,not iswhite,depth-1,-beta,-alpha,-neg)[1]
        board[move[0][0]][move[0][1]] = piece1
        board[move[1][0]][move[1][1]] = piece2
        if iswhite:
            if score==best_score:
                best_move.append(move)
            elif score>best_score:
                best_score = score
                best_move = [move]
            if best_score>alpha:
                alpha = best_score
            if alpha>=beta:
                break
        else:
            if score==best_score:
                best_move.append(move)
            elif score<best_score:
                best_score = score
                best_move = [move]
            if best_score>alpha:
                alpha = best_score
            if alpha>=beta:
                break
    if depth==DEPTH:
        return best_move,best_score
    else:
        return [],best_score
    """
    if depth==0:
        return [],neg*eval(board)
    if depth==DEPTH:
        best_move = []
    best_score = -HIGH
    move_set = get_moves(board,iswhite)
    for move in move_set:
        piece1 = board[move[0][0]][move[0][1]]
        piece2 = board[move[1][0]][move[1][1]]
        board[move[0][0]][move[0][1]] = "  "
        board[move[1][0]][move[1][1]] = piece1
        score = -minimax(board,not iswhite,depth-1,-beta,-alpha,-neg)[1]
        board[move[0][0]][move[0][1]] = piece1
        board[move[1][0]][move[1][1]] = piece2
        if score==best_score:
            if depth==DEPTH:
                best_move.append(move)
        elif score>best_score:
            best_score = score
            if depth==DEPTH:
                best_move = [move]
        if depth==DEPTH:
            if best_score>alpha:
                alpha = best_score
            if alpha>=beta:
                break
    if depth==DEPTH:
        return best_move,best_score
    else:
        return [],best_score

  
        
        if score>maxscore:
            maxscore = score
            if depth ==DEPTH:
                best_move = [move]
        """



    """
    move_set = get_moves(board,iswhite)
    if depth==0:
        return [],eval(board)
    if depth==DEPTH:
        best_move = []
    if iswhite:
        best_score = -HIGH
    else:
        best_score = HIGH
    for move in move_set:
        piece1 = board[move[0][0]][move[0][1]]
        piece2 = board[move[1][0]][move[1][1]]
        board[move[0][0]][move[0][1]] = "  "
        board[move[1][0]][move[1][1]] = piece1
        score = minimax(board,not iswhite,depth-1,-beta,-alpha)[1]
        board[move[0][0]][move[0][1]] = piece1
        board[move[1][0]][move[1][1]] = piece2
        if iswhite:
            if score==best_score:
                best_move.append(move)
            elif score>best_score:
                best_score = score
                best_move = [move]
            if best_score>alpha:
                alpha = best_score
            if alpha>=beta:
                break
        else:
            if score==best_score:
                best_move.append(move)
            elif score<best_score:
                best_score = score
                best_move = [move]
            if best_score>alpha:
                alpha = best_score
            if alpha>=beta:
                break
    if depth==DEPTH:
        return best_move,best_score
    else:
        return [],best_score
    """




