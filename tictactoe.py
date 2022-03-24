game_board = []


def make_board(n):
    """Make Board
    Make board for the game
    Args:
        n (int): board size

    Returns:
        list: board
    """
    return [['-' for count in range(n)] for rows in range(n)]


def print_board(board):
    """Print Board
    This function print board on terminal
    Args:
        board (list): a board list
    """
    for row in board:
        print(' '.join(row))
    print('')


def get_board_size():
    """Get Board Size
    This function is for the board size
    Returns:
        int: size
    """
    size = input("Enter board size (exemple 9)")
    return int(size)


def test(x: int, y: int):
    # n = get_board_size()
    myboard = make_board(3)
    myboard[x][y] = "X"
    print_board(myboard)


if __name__ == "__main__":
    import sys
    test(int(sys.argv[1]), int(sys.argv[2]))
