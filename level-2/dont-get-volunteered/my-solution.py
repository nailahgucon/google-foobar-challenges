def convert_coordinates(src):
    # Convert the source position to row and column coordinates
    row = src // 8
    col = src % 8
    return row, col

def shortest_path(start_row, start_col, board):
    # Perform breadth-first search to find the shortest path using a queue
    queue = [(start_row, start_col)]
    
    while queue:
        current_row, current_col = queue.pop(0)
        for move in [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]:
            # Generate new row and column coordinates based on knight's moves
            new_row = current_row + move[0]
            new_col = current_col + move[1]
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                if board[new_row][new_col] is None:
                    # Update the board with the minimum moves required to reach this position
                    board[new_row][new_col] = board[current_row][current_col] + 1
                    queue.append((new_row, new_col))
                    
def solution(src, dest):
    # Initialize the chessboard and convert source/destination positions to row and column coordinates
    board = [[None for _ in range(8)] for _ in range(8)]
    start_row, start_col = convert_coordinates(src)
    dest_row, dest_col = convert_coordinates(dest)
    board[start_row][start_col] = 0
    
    # Find the shortest path on the chessboard using breadth-first search
    shortest_path(start_row, start_col, board)
    
    # Return the minimum number of moves required to reach the destination position
    return board[dest_row][dest_col]