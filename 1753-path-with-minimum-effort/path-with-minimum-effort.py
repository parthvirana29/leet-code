import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        directions = [(1,0),(0,-1), (0,1), (-1,0)]
        effort = [[float('inf')] * m for _ in range(n)]
        effort[0][0] = 0
        print(effort)
        heap = [(0,0,0)]
        while (heap):
        
            curr_ef, row, col = heapq.heappop(heap)
            if (row == n-1 and col == m-1):
                return effort[row][col]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < n and 0 <= nc < m):
                    diff = abs(heights[nr][nc] - heights[row][col])
                    new_effort = max(curr_ef, diff)
                    if (new_effort < effort[nr][nc]):
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr,nc))
        return 0