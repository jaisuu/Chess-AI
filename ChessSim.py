import moves, boardobj, ChessAI,CAI


def main():
    board = boardobj.Boardobject()
    AI_white= True
    AI_black= True
    game_on = True
    white_turn = True
    print("State of the board")
    board.print_board()
    while game_on:
        if AI_white and white_turn:
            best_move = CAI.minimax_move(board.board,True,3) #(board.board,True)
            if best_move==None:
                print("Black wins")
                break
            print(best_move)
            board.move(best_move[0],best_move[1])
            

        else:
            best_move = CAI.random_move(board.board,False)
            if best_move==None:
                print("White wins")
                break
            print(best_move)
            board.move(best_move[0],best_move[1])
        """
        elif AI_black and not white_turn:
            best_move = CAI.minimax_move(board.board,False,2)
            board.move(best_move[0],best_move[1])
            print(best_move)
        """
        white_turn = not white_turn
       
        board.print_board()
        
    



if __name__=="__main__":
    main()




