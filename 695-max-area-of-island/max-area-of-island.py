from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1,0),(0,-1)]
        q = deque()
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        print(visited)
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] not in visited and grid[i][j] == 1:
                    # perform bfs
                    q.append((i,j))
                    # mark position as visited
                    visited[i][j] = 1
                    count = 1
                    while (q):
                        curr_row, curr_col = q.popleft()
                    
                        for dr, dc in directions:
                            nr, nc = curr_row + dr, curr_col + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and visited[nr][nc] != 1 and grid[nr][nc] == 1:
                                q.append((nr,nc))
                                visited[nr][nc] = 1
                                count += 1
                    max_area = max(max_area, count)
        return max_area

