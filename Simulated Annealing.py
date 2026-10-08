import random
import math

# ---------------------------------------
# Cost Function
# ---------------------------------------
def cost(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):

            # Same row
            if board[i] == board[j]:
                conflicts += 1

            # Same diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# ---------------------------------------
# Function to Print Chessboard
# ---------------------------------------
def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):

            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# ---------------------------------------
# Simulated Annealing
# ---------------------------------------
def simulated_annealing(n=8, T=10.0, alpha=0.99):

    # Generate random initial board
    board = [random.randint(0, n - 1) for _ in range(n)]

    current_cost = cost(board)

    while T > 0.001:

        # If solution is found
        if current_cost == 0:
            return board, current_cost

        # Create a new neighboring state
        new_board = board.copy()

        # Select random column
        col = random.randint(0, n - 1)

        # Select a different random row
        new_row = random.randint(0, n - 1)

        while new_row == new_board[col]:
            new_row = random.randint(0, n - 1)

        # Move queen
        new_board[col] = new_row

        # Calculate new cost
        new_cost = cost(new_board)

        # Calculate change in cost
        delta_E = new_cost - current_cost

        # Acceptance criterion
        if delta_E < 0:
            # Better solution -> always accept
            board = new_board
            current_cost = new_cost

        else:
            # Worse solution -> accept probabilistically
            probability = math.exp(-delta_E / T)
            R = random.random()

            if R < probability:
                board = new_board
                current_cost = new_cost

        # Cool down temperature
        T = T * alpha

    return board, current_cost


# ---------------------------------------
# Main Program
# ---------------------------------------

solution, final_cost = simulated_annealing()

print("Final Board:", solution)
print("Final Cost:", final_cost)

print("\nChess Board:")
print_board(solution)

if final_cost == 0:
    print("\nSolution Found!")
else:
    print("\nNo solution found.")
