import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0,0,0)]
        n = len(heights)
        m = len(heights[0])
        effort = [[float('inf')]* m for _ in range(n)]
        effort[0][0] = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while(heap):
            row, col, curr_effort = heapq.heappop(heap)
            if (row == n - 1 and col == m - 1):
                return effort[-1][-1]
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (0 <= nr < n and 0 <= nc < m):
                    new_diff = abs(heights[row][col] - heights[nr][nc])
                    new_effort = max(curr_effort, new_diff)
                    if (new_effort) < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (nr,nc,new_effort))
        return 0
            