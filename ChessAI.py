import moves, boardobj, random
class AI():
    def __init__(self,iswhite,board_obj):
        self.iswhite = iswhite
        self.boardobj = board_obj
        self.depth = 3

    def eval_state(self):
            board = self.boardobj.board
            score = 0
            for r in range(0,8):
                for c in range(0,8):
                    if board[r][c][0]=="W":
                        if board[r][c][1]=="Q":
                            score+=9
                        if board[r][c][1]=="B" or board[r][c][1]=="N":
                            score+=3
                        if board[r][c][1]=="R":
                            score+=5
                        if board[r][c][1]=="P":
                            score+=1
                    if board[r][c][0]=="B":
                        if board[r][c][1]=="Q":
                            score-=9
                        if board[r][c][1]=="B" or board[r][c][1]=="N":
                            score-=3
                        if board[r][c][1]=="R":
                            score-=5
                        if board[r][c][1]=="P":
                            score-=1
            return score
    def lol(self,iswhite):
        global nextmove
        nextmove = []
        self.minimax_move(iswhite,self.depth)
        if len(nextmove)>1:
            return nextmove[random.randrange(len(nextmove))]
        if len(nextmove)==0:
            return None
        return nextmove[0]
    def minimax_move(self,iswhite,depth):
        global nextmove
        if depth==0:
            return self.eval_state()
        if iswhite:
            maxscore = -40
            move_set = self.boardobj.get_moves()
            for move in move_set:
                self.boardobj.move(move[0],move[1])
                score = self.minimax_move(not iswhite,depth-1)
                if score==maxscore:
                    nextmove.append(move)
                if score>maxscore:
                    maxscore= score
                    if depth==self.depth:
                        nextmove= [move]
                
                self.boardobj.undo()
            return maxscore
        else:
            maxscore = 40
            move_set = self.boardobj.get_moves()
            for move in move_set:
                self.boardobj.move(move[0],move[1])
                score = self.minimax_move(not iswhite,depth-1)
                if score==maxscore:
                    nextmove.append(move)
                if score<maxscore:
                    maxscore= score
                    if depth==self.depth:
                        nextmove= [move]
                
                self.boardobj.undo()
            return maxscore
"""
        move_set = self.boardobj.get_moves()
        best_move = move_set[0]
        move = move_set[0]
        self.boardobj.move(move[0],move[1])
        best_score = self.eval_state()
        self.boardobj.undo()
        for move in move_set:
            score = self.minimax_score(self.iswhite,self.depth,move)
            if iswhite:
                if score>best_score:
                    best_move = move
                    best_score = score
                    
            else:
                if score<best_score:
                    best_move = move
                    best_score = score
        return best_move




    def minimax_score(self,iswhite,depth,move):
        if depth==0:
            return self.eval_state()
        if depth==self.depth:
            self.boardobj.move(move[0],move[1])
            score = self.minimax_score(not iswhite, depth-1,move)
            self.boardobj.undo()
            return score
        move_set = self.boardobj.get_moves()
        if iswhite:
            best_score = -40
            for amove in move_set:
                self.boardobj.move(amove[0],amove[1])
                score = self.minimax_score(not iswhite,depth-1,move)
                if score>best_score:
                    best_score = score
                self.boardobj.undo()
            return best_score
        else:
            best_score = 40
            for amove in move_set:
                self.boardobj.move(amove[0],amove[1])
                score = self.minimax_score(not iswhite,depth-1,move)
                if score>best_score:
                    best_score = score
                self.boardobj.undo()
            return best_score 

        
"""
                    
