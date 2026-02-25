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
        visited = set()

        print("Start queue: ", queue)
        print("Start visited: ", visited)
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        while (queue):
            curr = queue.popleft()
            i, j, pathlength = curr
            if i + 1 == rows and j + 1 == cols:
                return pathlength
            visited.add(curr)
            nodeSeen = False
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 0):
                    queue.append((nr,nc, pathlength + 1))
                    visited.add((nr,nc))
        return -1
                
