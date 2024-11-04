def print_board(board, n):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    # Base case: If all queens are placed
    if row >= n:
        return True

    # Consider this row and try placing the queen in all columns
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False

def n_queens(n):
    # Initialize the board
    board = [[0] * n for _ in range(n)]

    # Solve the problem
    if solve_n_queens(board, 0, n):
        print("One of the solutions:")
        print_board(board, n)
    else:
        print("No solution exists for the given board size.")

# Main program loop
while True:
    try:
        n = int(input("Enter the size of the chessboard (n for n-Queens): "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            continue

        # Solve the n-Queens problem
        n_queens(n)

    except ValueError:
        print("Invalid input. Please enter an integer.")

    # Check if the user wants to continue or exit
    choice = input("Do you want to solve another n-Queens problem? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Exiting program.")
        break
