class Boardobject():
    def __init__(self,board):
        self.board = board
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

