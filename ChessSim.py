import moves,board_object,ChessAI
import sys
board = [["BR","BN","BB","BQ","BK","BB","BN","BR"],
         ["BP","BP","BP","BP","BP","BP","BP","BP"],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["WP","WP","WP","WP","WP","WP","WP","WP"],
         ["WR","WN","WB","WQ","WK","WB","WN","WR"]]
def print_board(board1):
    for i in range(0,8):
        print("["+board1[i][0],end="")
        for j in range(1,8):
            print(","+str(board1[i][j]),end="")
        print("]")
def valid_moves(state,iswhite):
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
    return moveset
def main():
    game_on = True
    state = board_object.Boardobject(board)
    player1 = True
    player2 = False
    numplayers = 0
    iswhite = True
    AI = ChessAI.AI(state, not iswhite)
    AI2 = ChessAI.AI(state,iswhite)
    while game_on:
        validmoves = valid_moves(state,iswhite)
        #print(validmoves)
        if(len(validmoves))==0:
            game_on = False
            break
        AI.board = state.board
        AI2.board = state.board
        print(str(AI.eval(state.board)))
        print_board(state.board)
        print("\n")
        if iswhite:
            AI2.makemini()
            iswhite = not iswhite
        else:
            AI.makemini()
            iswhite = not iswhite
        
        




if __name__=="__main__":
    main()



