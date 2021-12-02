import moves
board = [["BR","BN","BB","BQ","BK","BB","BN","BR"],
         ["BP","BP","BP","BP","BP","BP","BP","BP"],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["WP","WP","WP","WP","WP","WP","WP","WP"],
         ["WR","WN","WB","WQ","WK","WB","WN","WR"]]

board1 =[["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","BR","  "],
         ["  ","  ","BP","  ","  ","  ","  ","BQ"],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","WN","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "]]

class Boardobject():
    def __init__(self):
        self.board = board1
        self.white = True
        self.bcan_castle = True
        self.wcan_castle = True
        self.lBR_moved = False
        self.rBR_moved = False
        self.lWR_moved = False
        self.rWR_moved = False
        self.BK_moved = False
        self.WK_moved = False
        self.advanced_2 = []
        self.en_passant = []
        self.moves = []

    def get_moves(self):
        move_set = []
        for r in range(0,8):
            for c in range(0,8):
                if self.white:
                    if self.board[r][c][0]=="W":
                        if self.board[r][c][1]=="K":
                            move_set+=moves.king_moves(r,c,self.board,True)
                        if self.board[r][c][1]=="Q":
                            move_set+=moves.queen_moves(r,c,self.board,True)
                        if self.board[r][c][1]=="B":
                            move_set+=moves.bishop_moves(r,c,self.board,True)
                        if self.board[r][c][1]=="N":
                            move_set+=moves.knight_moves(r,c,self.board,True)
                        if self.board[r][c][1]=="R":
                            move_set+=moves.rook_moves(r,c,self.board,True)
                        if self.board[r][c][1]=="P":
                            move_set+=moves.pawn_moves(r,c,self.board,True)
                else:
                    if self.board[r][c][0]=="B":
                        if self.board[r][c][1]=="K":
                            move_set+=moves.king_moves(r,c,self.board,False)
                        if self.board[r][c][1]=="Q":
                            move_set+=moves.queen_moves(r,c,self.board,False)
                        if self.board[r][c][1]=="B":
                            move_set+=moves.bishop_moves(r,c,self.board,False)
                        if self.board[r][c][1]=="N":
                            move_set+=moves.knight_moves(r,c,self.board,False)
                        if self.board[r][c][1]=="R":
                            move_set+=moves.rook_moves(r,c,self.board,False)
                        if self.board[r][c][1]=="P":
                            move_set+=moves.pawn_moves(r,c,self.board,self.white)
        return move_set


    def print_board(self):
        for i in range(0,8):
            print("["+self.board[i][0],end="")
            for j in range(1,8):
                print(","+str(self.board[i][j]),end="")
            print("]")

    def move(self,start,end):
        self.moves.append((start,end,self.board[start[0]][start[1]],self.board[end[0]][end[1]]))
        self.board[end[0]][end[1]]=self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = "  "
        self.white = not self.white
        

    def undo(self):
        move = self.moves.pop()
        start = move[0]
        end = move[1]
        piece1 = move[2]
        piece2 = move[3]
        self.board[start[0]][start[1]] = piece1
        self.board[end[0]][end[1]] = piece2
        self.white = not self.white

