import os
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_board(rows, cols):
    import random
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


def print_board(board):
    for row in board:
        print(' '.join(['■' if cell else ' ' for cell in row]))
    print()


def count_neighbors(board, x, y):
    rows, cols = len(board), len(board[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < rows and 0 <= y + j < cols:
                count += board[x + i][y + j]
    return count


def update_board(board):
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
            else:
                if neighbors == 3:
                    new_board[i][j] = 1
    return new_board


def main(rows, cols, generations, delay):
    board = initialize_board(rows, cols)
    for _ in range(generations):
        clear_console()
        print("Generation:", _ + 1)
        print_board(board)
        board = update_board(board)
        time.sleep(delay)


if __name__ == "__main__":
    rows = 20
    cols = 20
    generations = 50
    delay = 0.5

    main(rows, cols, generations, delay)
