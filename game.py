from math import sqrt
### Game State Representation ###
BLANK = 0
WALL = 1
BOX = 2
KEEPER = 3
GOAL = 4
BOXPLUSGOAL = 5
KEEPERPLUSGOAL = 6

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

hashmap ={
    BLANK: ' ',
    WALL: '#',
    BOX: '$',
    KEEPER: '@',
    GOAL: '.',
    BOXPLUSGOAL: '*',
    KEEPERPLUSGOAL: '+'
}


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
    
        

class Board(Rules):
    def __init__(self, rows = 6, cols = 9):
        self.rows = rows
        self.cols = cols
        self.board =self.__fillBoard()
        self.goals = self.__goal_coordinates()
        self.keeper = self.__keeper_coordinates()
    
    def __fillBoard(self):
        ### Inititalize a board with preset values ###
        rboard = [
            [BLANK, BLANK, WALL, WALL, WALL, WALL, BLANK, BLANK, BLANK],
            [WALL, WALL, WALL, BLANK, BLANK, WALL, WALL, WALL, WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BOX, BLANK, WALL],
            [WALL, BLANK, WALL, BLANK, BLANK, WALL, BOX, BLANK, WALL],
            [WALL, BLANK, GOAL, BLANK, GOAL, WALL, KEEPER, BLANK, WALL],
            [WALL] * 9
        ]
        return rboard
    
    ### update keeper coordinates ###
    def update(self, direction):
        row, col = self.keeper
        row += direction[0]
        col += direction[1]
        self.keeper = (row, col)

    ### Starting the game will always provide keeper position ###
    def __keeper_coordinates(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == KEEPER:
                    return (i,j)

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
    