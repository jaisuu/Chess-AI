import random,moves
class AI:
    def __init__(self,state,iswhite):
        self.board = state.board
        self.iswhite = iswhite
        self.movelog = []
        self.validmoves = []
        self.state = state
        self.points = {"P":1,"N":3,"B":3,"R":5,"Q":9,"K":90," ":0}
    def castle(self,state,iswhite):
        return moves.castle(self.board,self.state,self.iswhite)
    def do_castle(self,pos1,pos2,board):
        state = self.state
        if pos1==(0,4):
            state.BK_moved=True
            if pos2==(0,0):
                state.lBR_moved = True
                state.board[0][0]="  "
                state.board[0][4]="  "
                state.board[0][2]="BK"
                state.board[0][3]="BR"
            if pos2==(0,7):
                state.rBR_moved = True
                state.board[0][7]="  "
                state.board[0][4]="  "
                state.board[0][6]="BK"
                state.board[0][5]="BR"
        if pos1==(7,4):
            state.WK_moved = True
            if pos2==(7,0):
                state.lWR_moved = True
                state.board[7][0]="  "
                state.board[7][4]="  "
                state.board[7][2]="WK"
                state.board[7][3]="WR"
            if pos2==(7,7):
                state.rWR_moved = True
                state.board[7][7]="  "
                state.board[7][4]="  "
                state.board[7][6]="WK"
                state.board[7][5]="WR"
    def valid_moves(self,state,iswhite):
        moveset = []
        for r in range(0,8):
            for c in range(0,8):
                if state.board[r][c][1]=="P":
                    moveset+=moves.pawn_moves(r,c,state.board,iswhite)
                elif state.board[r][c][1]=="R":
                    moveset+=moves.rook_moves(r,c,state.board,iswhite)
                elif state.board[r][c][1]=="N":
                    moveset+=moves.knight_moves(r,c,state.board,iswhite)
                elif state.board[r][c][1]=="B":
                    moveset+=moves.bishop_moves(r,c,state.board,iswhite)
                elif state.board[r][c][1]=="Q":
                    moveset+=moves.queen_moves(r,c,state.board,iswhite)
                elif state.board[r][c][1]=="K":
                    moveset+=moves.king_moves(r,c,state.board,iswhite,state)
        self.validmoves = moveset
    def move(self,pos1,pos2):
        state = self.state
        piece_moved = state.board[pos1[0]][pos1[1]]
        piece_captured = state.board[pos2[0]][pos2[1]]
        castle_moves = self.castle(self.state,self.iswhite)
        if (pos1,pos2) in castle_moves:
            self.do_castle(pos1,pos2,state.board)
            print("castle")
        else:
            state.board[pos2[0]][pos2[1]] = state.board[pos1[0]][pos1[1]]
            state.board[pos1[0]][pos1[1]] = "  " 
        #self.iswhite = not self.iswhite
        self.movelog.append((pos1,pos2,piece_moved,piece_captured))
    def undo(self):
        if len(self.movelog)>0:
            last_move = self.movelog.pop()
            r1,c1 = last_move[0]
            r2,c2 = last_move[1]
            if self.board[r1][c1]=="  " and self.board[r2][c2]=="  ":
                if r1==0 and c2==0:
                    self.board[0][0]="BR"
                    self.board[0][4]="BK"
                    self.board[0][1]="  "
                    self.board[0][2]="  "
                    self.board[0][3]="  "
                elif r1==0:
                    self.board[0][7]="BR"
                    self.board[0][4]="BK"
                    self.board[0][5]="  "
                    self.board[0][6]="  "
                elif r1==7 and c2==0:
                    self.board[7][0]="WR"
                    self.board[7][4]="WK"
                    self.board[7][1]="  "
                    self.board[7][2]="  "
                    self.board[7][3]="  "
                else:
                    self.board[7][7]="WR"
                    self.board[7][4]="WK"
                    self.board[7][5]="  "
                    self.board[7][6]="  "
            else:
                piece_moved = last_move[2]
                piece_captured = last_move[3]
                self.board[r1][c1] = piece_moved
                self.board[r2][c2] = piece_captured
        #self.iswhite = not self.iswhite
    def make_random(self):
        self.valid_moves(self.state,self.iswhite)
        randomnum = random.randint(0, len(self.validmoves)-1)
        self.move(self.validmoves[randomnum][0],self.validmoves[randomnum][1])
    def makemini(self):
        move = self.findbestminimax(3,self.iswhite)
        self.move(move[0],move[1])
    def findbestminimax(self,depth,iswhite):
        bestmove = None
        bestmove = self.findminimax(depth,iswhite,None)[1]
        return bestmove
    def findminimax(self,depth,iswhite,move):
        if depth==0:
            return self.eval(self.board),move
        else:
            if iswhite:
                max = -130
             
                self.valid_moves(self.state,iswhite)
                bestmove = self.validmoves[0]
                for move in self.validmoves:
                    self.move(move[0],move[1])
                    curr_eval = self.findminimax(depth-1,not iswhite,move)
                    if curr_eval[0]>max:
                        bestmove = curr_eval[1]
                    self.undo()
                return self.eval(self.board),bestmove
            else:
                max = 130
                self.valid_moves(self.state,iswhite)
                bestmove = self.validmoves[0]
                for move in self.validmoves:
                    self.move(move[0],move[1])
                    curr_eval = self.findminimax(depth-1,not iswhite,move)
                    if curr_eval[0]<max:
                        bestmove = curr_eval[1]
                    self.undo()
                return self.eval(self.board),bestmove
    def eval(self,board):
        score = 0
        for r in range(0,8):
            for c in range(0,8):
                if board[r][c][0]=="W":
                    score+=self.points[board[r][c][1]]
                else:
                    score-=self.points[board[r][c][1]]
        return score
                    

"""
        if(iswhite):
            print("White's turn")
        else:
            print("Black's turn")
        if iswhite:
            pos1,pos2 = input("Your turn, input your move ie. startrow,startcol endrow,endcol: ").split()
            pos1 = (int(pos1[0]),int(pos1[2]))
            pos2 = (int(pos2[0]),int(pos2[2]))
            if(pos1==(9,9)):
                AI.undo()
                print_board(state.board)
                pos1,pos2 = input("Your turn, input your move ie. startrow,startcol endrow,endcol: ").split()
                pos1 = (int(pos1[0]),int(pos1[2]))
                pos2 = (int(pos2[0]),int(pos2[2]))
            castle_moves = moves.castle(state.board,state,iswhite)
        
            
            if (pos1,pos2) in validmoves:
                if (pos1,pos2) in castle_moves:
                    if pos1==(0,4):
                        state.BK_moved=True
                        if pos2==(0,0):
                            state.lBR_moved = True
                            state.board[0][0]="  "
                            state.board[0][4]="  "
                            state.board[0][2]="BK"
                            state.board[0][3]="BR"
                        if pos2==(0,7):
                            state.rBR_moved = True
                            state.board[0][7]="  "
                            state.board[0][4]="  "
                            state.board[0][6]="BK"
                            state.board[0][5]="BR"
                    if pos1==(7,4):
                        state.WK_moved = True
                        if pos2==(7,0):
                            state.lWR_moved = True
                            state.board[7][0]="  "
                            state.board[7][4]="  "
                            state.board[7][2]="WK"
                            state.board[7][3]="WR"
                        if pos2==(7,7):
                            state.rWR_moved = True
                            state.board[7][7]="  "
                            state.board[7][4]="  "
                            state.board[7][6]="WK"
                            state.board[7][5]="WR"
                else:
                    state.board[pos2[0]][pos2[1]] = state.board[pos1[0]][pos1[1]]
                    state.board[pos1[0]][pos1[1]] = "  " 
                iswhite = not iswhite
            else:
                print("Invalid move")
"""