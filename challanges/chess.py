import numpy as np

class cell:

    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist


# is valid move
def is_valid_move(x, y, size):
    if 1 <= x <= size and 1 <= y <= size:
        return True
    return False


# Method returns minimum step to reach
# target position
def minStepToReachTarget(start_row, start_col, target_row, target_col, size):

    #all possible movments for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []
    # push starting position of knight
    # with 0 distance
    queue.append(cell(start_row, start_col, 0))

    # make all cell unvisited
    # visited = [[False for i in range(size + 1)] for j in range(size + 1)]
    visited = np.zeros((size, size), dtype=bool)
    visited = [[False]*(size+1) for i in range(size+1)]
    # visit starting state
    visited[start_row][start_col] = True

    # loop untill we have one element in queue
    while len(queue) > 0:
        t = queue[0]
        print("t = ", queue[0])
        queue.pop(0)

        # if current cell is equal to target
        # cell, return its distance
        if t.x == target_row and t.y == target_col:
            return t.dist

        # iterate for all reachable states
        for i in range(8):

            x = t.x + dx[i]
            y = t.y + dy[i]

            if(is_valid_move(x, y, size) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))

# Driver Code
if __name__=='__main__':
    n = 8
    start_row_val, start_col_val = 4, 4
    target_row_val, target_col_val = 4, 8
    print(minStepToReachTarget(start_row_val, start_col_val, target_row_val, target_col_val, n))
