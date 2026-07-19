class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        top = (-1,0)
        left = (0,-1)
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                cur_top = grid[i-1][j] if i-1 >= 0 else float('inf')
                cur_left = grid[i][j-1] if j - 1 >= 0 else float('inf')

                if cur_top == float('inf') and cur_left == float('inf'):
                    print("row: ", i, "col: ", j)
                    continue
                print(cur_left, cur_top)
                grid[i][j] = grid[i][j] + min(cur_top, cur_left)
        print(grid)
        return grid[row-1][col-1]

