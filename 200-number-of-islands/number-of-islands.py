from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]* cols for i in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        print(visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    # perform BFS
                    queue = deque([(i,j)])
                    visited[i][j] = True
                    while (queue):
                        print("I get in here")
                        curr = queue.popleft()
                        row, col = curr
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and not visited[nr][nc]):
                                queue.append((nr,nc))
                                visited[nr][nc] = True
                    numIslands += 1
        return numIslands
                            

                        
 