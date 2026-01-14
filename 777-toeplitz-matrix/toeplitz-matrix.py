class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # maxLimit = min(len(matrix),len(matrix[0]))
        # curr = 0
        # prevElement = matrix[curr][curr]
        # while (curr < maxLimit):
        #     currElement = matrix[curr][curr]
        #     if (currElement != prevElement):
        #         return False            
        #     prev = matrix[curr][curr]
        #     curr += 1

        for i in matrix:
            print(i)
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
               
                if (matrix[i-1][j-1] != matrix[i][j]):
                    return False



        return True
