import copy
from game import Board, Rules, BOXPLUSGOAL, UP, DOWN, LEFT, RIGHT, BOX, KEEPERPLUSGOAL, KEEPER, GOAL
############### START of helper Functions ##############################################
### Give this function a copy don't modify the input state ###
"""
input: state of the board, row, column, and value to replace
returns: state of the board 
"""
def set_square(s, r, c, v):
     s.board[r][c] = v
     return s

"""
input: Direction of the move
returns: None or a new state of the board
uses: Rules class to determain vadility of the move
      move_box function -> if the keeper moves the box then both the box and keeper must move
      set_square function -> set the new location of the keeper
      clean_validate function -> if on a goal the keeper must move and the goal must return to a .
"""
def try_move(s, d):
    ### Check if your current pos is the keeper and goal ###
    current = Rules.iskeeperplusgoal(s.board, s.keeper[0], s.keeper[1])
    new_row, new_col = s.keeper
    new_row += d[0]
    new_col += d[1]
    if Rules.iswall(s.board, new_row, new_col):
         return None         
    elif Rules.isbox(s.board,new_row, new_col):
        check = move_box(s, (new_row, new_col), d)
        if check:
            cleanvalidate(s, d, current)
            return set_square(s, new_row, new_col, KEEPER)
        return None
    elif Rules.isgoal(s.board, new_row, new_col):
        cleanvalidate(s, d, current)
        return set_square(s, new_row, new_col, KEEPERPLUSGOAL)
    elif Rules.isboxplusgoal(s.board, new_row, new_col):
        check = move_box(s, (new_row, new_col), d)
        if check:
            cleanvalidate(s, d, current)
            return set_square(s, new_row, new_col, KEEPERPLUSGOAL)
        return check
    else:
        cleanvalidate(s, d, current)
        return set_square(s, new_row, new_col, KEEPER)
    
     
### update and validate the keeper position ###
""" 
use case: validates if the current state of the keeper should a BLANK state next or a GOAL state
          used as a helper function when checking for moves.
returns: new state of the board
"""
def cleanvalidate(state, direction, curr):
    row, col = state.keeper
    if curr:
        state.update(direction)
        state = set_square(state, row, col, GOAL)
    else:
        state.update(direction)
    return state 

### Function to move box ###
"""
returns: None or the new state of the board
"""
def move_box(state, position, direction):
        ### Get coordinates for direction of the box ###
        new_row, new_col = position
        new_row += direction[0]
        new_col += direction[1]
        ### Check for move vadility ###
        if Rules.iswall(state.board, new_row, new_col) or Rules.isbox(state.board, new_row, new_col) or Rules.isboxplusgoal(state.board, new_row, new_col) or Rules.isbounded(state.rows, state.cols, new_row, new_col):
            return None
        elif Rules.isgoal(state.board, new_row, new_col):
            return set_square(state, new_row, new_col, BOXPLUSGOAL)
        
        return set_square(state, new_row, new_col, BOX)
### EOF function to move box ###


### Hueristic backtracking helper ###
def match(distances, boxes, box_index, used_goals):
    ### Base Case ###
    if box_index == len(boxes):
        return 0
    
    best = float('inf')
    box = boxes[box_index]

    ### try all goals ###
    for goal_index in range(len(distances[box])):
        if goal_index not in used_goals:
            cost = distances[box][goal_index]
            total = cost + match(distances, boxes, box_index + 1, used_goals | {goal_index})
            best = min(best, total)
    return best
     
################ End of Helper Functions ######################################
################ START of calibrator Functions ######################################
def goal_test(state):
        coordinates = state.goals
        for coord in coordinates:
            row, col = coord
            if state.board[row][col] != BOXPLUSGOAL:
                return False
        return True

def next_states(state):
    possible_moves = [UP, DOWN, LEFT, RIGHT]
    states = list()
    for move in possible_moves:
        # Filter invalid moves #
        new_state = try_move(copy.deepcopy(state), move)
        if new_state:
            states.append(new_state)
    return states

### Hueristic is admissible if it returns 0 ###
### Returning 0 means it never overestimates anything ###
def h0(state):
     return 0

### new Admissibe Heuristic ###
"""
Manhattan distance: Find the closest box distance to each goal
                    Number of grid steps ignoring obstacles 
"""
def h403967197(state):
    ### Find boxes biult in function in class ###
    boxes = list()
    boxes = state.find_box()
    goals = state.goals
    ### Find the goal
    ### Find the distance between boxes and goals ###
    distances = {}
    for box in boxes:
        box_row, box_col = box
        distances[box] = list()
        for goal in goals:
            goal_row, goal_col = goal 
            distance = abs(box_row - goal_row) + abs(box_col - goal_col)
            distances[box].append(distance)
        
    return match(distances, boxes, 0, set())


### Heurisitc function: returns number of boxes not in goal positions###
"""
This hueristic is admissible because each box not on a goal
must be moved at least once before the puzzle can be solved,
so it never over estimates it's true cost
"""
def h1(state):
    count = 0
    for i in range(state.rows):
        for j in range(state.cols):
            if state.board[i][j] == BOX:
                count += 1
    return count 

### cost function ###
def cost_fn(state1, state2):
    return 1

"""Test"""
def main():
    state = Board()
    state.printBoard()
    print(h403967197(state))
    
    


if __name__ == "__main__":
    main()