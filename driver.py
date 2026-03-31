import copy
from game import Board, Rules, BOXPLUSGOAL, WALL, UP, DOWN, LEFT, RIGHT, BOX, KEEPERPLUSGOAL, KEEPER
### Helper Functions ###
def get_square(s, r, c):
     if (0 <= r < s.rows) and (0 <= c < s.cols):
        return s.board[r][c]
     return WALL 
### Give this function a copy don't modify the input state ###
def set_square(s, r, c, v):
     s.board[r][c] = v
     return s
### Function to try moves ###
def try_move(s, d):
    new_row, new_col = s.keeper
    new_row += d[0]
    new_col += d[1]
    if Rules.iswall(s.board, new_row, new_col):
         return None
    elif Rules.isbox(s.board,new_row, new_col):
        check = move_box(s, (new_row, new_col), d)
        if check:
             return set_square(s, new_row, new_col, KEEPER)
    elif Rules.isgoal(s.board, new_row, new_col):
        return set_square(s, new_row, new_col, KEEPERPLUSGOAL)
    elif Rules.isboxplusgoal(s.board, new_row, new_col):
        check = move_box(s, (new_row, new_col), d)
        if check:
            return set_square(s, new_row, new_col, KEEPERPLUSGOAL)
        return check
    else:
         return set_square(s, new_row, new_col, KEEPER)
    
     

### Function to move box ###
def move_box(state, position, direction):
        ### check for invalid move ###
        new_row, new_col = position
        new_row += direction[0]
        new_col += direction[1]
        if Rules.iswall(state.board, new_row, new_col) or Rules.isbox(state.board, new_row, new_col) or Rules.isboxplusgoal(state.board, new_row, new_col) or Rules.isbounded(state.rows, state.cols, new_row, new_col):
            return None
        if Rules.isgoal(state.board, new_row, new_col):
             return set_square(state, new_row, new_col, BOXPLUSGOAL)
        return set_square(state, new_row, new_col, BOX)

     

def goal_test(state):
        coordinates = state.goals
        for coord in coordinates:
            row, col = coord
            if state.board[row][col] != BOXPLUSGOAL:
                return False
        return True

def next_states(state):
    """
    returns: list of all states that can be reached 
    """

def main():
    state = Board()
    state.printBoard()
    print(try_move(state, RIGHT))
    state.update(direction=RIGHT)
    print(try_move(state, UP))
    state.update(direction=UP)
    print(try_move(state, UP))
    state.update(direction=UP)
    print(try_move(state, LEFT))
    state.update(direction=LEFT)
    state.printBoard()


if __name__ == "__main__":
    main()