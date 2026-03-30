from math import sqrt
### Game State Representation ###
BLANK = 0
WALL = 1
BOX = 2
KEEPER = 3
GOAL = 4
BOXPLUSGOAL = 5
KEEPERPLUSGOAL = 6

hashmap ={
    BLANK: ' ',
    WALL: '#',
    BOX: '$',
    KEEPER: '@',
    GOAL: '.',
    BOXPLUSGOAL: '*',
    KEEPERPLUSGOAL: '+'
}

def goal_test(board):
        coordinates = board.goals
        for coord in coordinates:
            row, col = coord
            if board.board[row][col] != BOXPLUSGOAL:
                return False
        return True

class Rules:
    ### Board Checks ###
    """
    Checks current position vs board bounds
    To check if the move is bounded
    """
    def isbounded(bRow, bCol, row, col):
        valid = bRow <= row and bCol <= col
        return valid
    
    def isblank(board, row, col):
        return board[row][col] == BLANK
    
    def iswall(board, row, col):
        return board[row][col] == WALL
    
    def isbox(board, row, col):
        return board[row][col] == BOX
    
    def iskeeper(board, row, col):
        return board[row][col] == KEEPER
    
    def isgoal(board, row, col):
        return board[row][col] == GOAL
    
    def isboxplusgoal(board, row, col):
        return board[row][col] == BOXPLUSGOAL
    
    def iskeeperplusgoal(board, row, col):
        return board[row][col] == KEEPERPLUSGOAL
    
    ### Player Rules ###
    def __distance(curr_pos, next_pos):
        x1,y1 = curr_pos
        x2,y2 = next_pos
        return (sqrt((x2 - x1)**2 + (y2-y1)**2) < 2)
    
    def canwalk(self, curr_pos, next_pos):
        distance = self.__distance(curr_pos, next_pos)
        return (curr_pos == KEEPER and next_pos == BLANK and distance)
    
    def canpush(self, curr_pos, next_pos):
        distance = self.__distance(curr_pos, next_pos)
        return (curr_pos == KEEPER and next_pos == BOX and distance)
    
    
    
            
    
    

class Board(Rules):
    def __init__(self, rows = 6, cols = 9):
        self.rows = rows
        self.cols = cols
        self.board =self.__emptyBoard()
        self.goals = self.__goal_coordinates()
    
    def __emptyBoard(self):
        ### Inititalize a board with all BLANK values ###
        rboard = [
            [BLANK, BLANK, WALL, WALL, WALL, WALL, BLANK, BLANK, BLANK],
            [WALL, WALL, WALL, BLANK, BLANK, WALL, WALL, WALL, WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BOX, BLANK, WALL],
            [WALL, BLANK, WALL, BLANK, BLANK, WALL, BOX, BLANK, WALL],
            [WALL, BLANK, GOAL, BLANK, GOAL, WALL, KEEPER, BLANK, WALL],
            [WALL] * 9
        ]
        return rboard
    def __goal_coordinates(self):
        coordinates = list()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == GOAL:
                    coordinates.append((i,j))
        return coordinates
    
    def printBoard(self):
        print(self.board)
        for i in range(self.rows):
            for j in range(self.cols):
                key = self.board[i][j]
                print(hashmap[key], end="")
            print()
    