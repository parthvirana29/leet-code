class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # frist transformation (flip @ 180):
        for i in range(len(matrix)//2):
            # only swap till half way
            for j in range(len(matrix[0])):
                a = matrix[i][j]
                matrix[i][j] = matrix[len(matrix)-i-1][j]
                matrix[len(matrix)-i-1][j] = a

        print(matrix)

        # second transformation (flip @ 315)
        for i in range(len(matrix)):
            # only swap till half way
            for j in range(i+1, len(matrix[0])):
                # skip the diagonal
                if i == j:
                    continue
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a
        print(matrix)
                

        