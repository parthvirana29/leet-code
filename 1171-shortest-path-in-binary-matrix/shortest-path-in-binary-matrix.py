from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        if (grid[0][0] != 0 or grid[rows-1][cols-1] != 0):
            return -1
        
        pathLength = 0
        # adding 1 as default path length
        queue = deque([(0,0,1)])
        # use 2D matrix instead of a set of tuples because tuples are hashed carrying significant overhead
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True

        print("Start queue: ", queue)
        print("Start visited: ", visited)
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        while (queue):
            curr = queue.popleft()
            i, j, pathlength = curr
            if i + 1 == rows and j + 1 == cols:
                return pathlength
            visited[i][j] = True
            nodeSeen = False
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0):
                    queue.append((nr,nc, pathlength + 1))
                    visited[nr][nc] = True
        return -1
                
