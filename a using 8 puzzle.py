def get_misplaced_tiles(board, goal_board):
    misplaced = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] != 0:
                if board[r][c] != goal_board[r][c]:
                    misplaced += 1
    return misplaced

def find_blank_space(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return r, c

def get_next_moves(board):
    moves = []
    r, c = find_blank_space(board)
    directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    
    for dr, dc, move_name in directions:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_board = [list(row) for row in board]
            new_board[r][c], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[r][c]
            moves.append((move_name, tuple(tuple(row) for row in new_board)))
            
    return moves

def solve_puzzle(start_board, goal_board):
    h_start = get_misplaced_tiles(start_board, goal_board)
    open_list = [[h_start, 0, start_board, []]]
    visited = set()
    
    while open_list:
        open_list.sort(key=lambda x: x)  # Picks lowest f(n) value
        f, g, current_board, moves_taken = open_list.pop(0)
        
        if current_board == goal_board:
            return moves_taken
            
        if current_board in visited:
            continue
        visited.add(current_board)
        
        for move_name, next_board in get_next_moves(current_board):
            if next_board not in visited:
                new_g = g + 1
                new_h = get_misplaced_tiles(next_board, goal_board)
                new_f = new_g + new_h
                open_list.append([new_f, new_g, next_board, moves_taken + [move_name]])
                
    return None

def input_matrix(state_name):
    print(f"Enter {state_name} state (3 numbers per row separated by spaces):")
    user_board = []
    for i in range(3):
        row_input = input(f"Row {i+1}: ")
        row = [int(x) for x in row_input.split()]
        user_board.append(row)
    return tuple(tuple(row) for row in user_board)

if __name__ == "__main__":
    initial_state = input_matrix("initial")
    goal_state = input_matrix("goal")
    
    print("\nProcessing...")
    result_moves = solve_puzzle(initial_state, goal_state)
    
    if result_moves is not None:
        print("Moves:", " -> ".join(result_moves))
        print("Total Cost:", len(result_moves))
    else:
        print("No solution found.")
