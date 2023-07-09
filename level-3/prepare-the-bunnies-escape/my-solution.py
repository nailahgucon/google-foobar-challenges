def solution(maze):
    width = len(maze[0])  
    height = len(maze)  
    
    ### breadth-first search to find the shortest path from the top-left corner to each cell in the maze
    board = [[None for i in range(width)] for i in range(height)]  # Initialize a board to store the path lengths
    board[0][0] = 1  # starting position = 1
    queue = [(0, 0)]  # Initialize a queue with starting position
    while queue:
        x, y = queue.pop(0)  # Get the next position from the queue
        for move in [[1, 0], [-1, 0], [0, -1], [0, 1]]:  # Check all possible moves: down, up, left, right
            new_x, new_y = x + move[0], y + move[1]  # Calculate the new position
            if 0 <= new_x < height and 0 <= new_y < width:  # Check if the new position is within the maze boundaries
                if board[new_x][new_y] is None:  # Check if the new position has not been visited
                    board[new_x][new_y] = board[x][y] + 1  # Update the path length to the new position
                    if maze[new_x][new_y] == 1:  # Check if the new position is a wall
                        continue  # Skip the wall and continue with the next move
                    queue.append((new_x, new_y))  # Add the new position to the queue
    top_bottom = board  # Store the shortest path
    
    ### breadth-first search to find the shortest path from the bottom-right corner to each cell in the maze
    board = [[None for j in range(width)] for j in range(height)]  # Reset the board
    board[height-1][width-1] = 1  # ending position = 1
    queue = [(height-1, width-1)]  # Initialize a queue with ending position
    while queue:
        x, y = queue.pop(0)  # Get the next position from the queue
        for move in [[1, 0], [-1, 0], [0, -1], [0, 1]]:  # Check all possible moves: down, up, left, right
            new_x, new_y = x + move[0], y + move[1]  # Calculate the new position
            if 0 <= new_x < height and 0 <= new_y < width:  # Check if the new position is within the maze boundaries
                if board[new_x][new_y] is None:  # Check if the new position has not been visited
                    board[new_x][new_y] = board[x][y] + 1  # Update the path length to the new position
                    if maze[new_x][new_y] == 1:  # Check if the new position is a wall
                        continue  # Skip the wall and continue with the next move
                    queue.append((new_x, new_y))  # Add the new position to the queue
    bottom_top = board  # Store the shortest path

    min_path = 2 ** 32 - 1  # Initialize the minimum path length with a large value
    for i in range(height):
        for j in range(width):
            if top_bottom[i][j] and bottom_top[i][j]:  # Check if there is a path from both top to bottom and bottom to top
                min_path = min(top_bottom[i][j] + bottom_top[i][j] - 1, min_path)  # Calculate the minimum path length
    return min_path  # Return the minimum path length