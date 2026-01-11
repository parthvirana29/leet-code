class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for x in range(n)] for y in range (n)]
        top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        iterator = 1
        while (top <= bottom and left <= right):
            # top: left --> right
            for i in range(left, right+1):
                matrix[top][i] = iterator
                iterator += 1
            top += 1
            # right: top --> bottom
            for i in range(top, bottom+1):
                matrix[i][right] = iterator
                iterator += 1
            right -= 1
            # bottom: right --> left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = iterator
                iterator += 1
            bottom -= 1
            # left: bottom --> up
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = iterator
                iterator += 1
            left += 1
        return matrix
            


            
            


            