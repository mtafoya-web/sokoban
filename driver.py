from game import Board, goal_test


def main():
    new_board = Board()
    new_board.printBoard()
    print(goal_test(new_board))


if __name__ == "__main__":
    main()