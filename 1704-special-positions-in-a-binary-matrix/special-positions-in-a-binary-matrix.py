class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        for row in range(len(mat)):
            if sum(mat[row]) == 1:
                col = mat[row].index(1)
                colSum = 0
                print("col: ", col)
                for i in range(len(mat)):
                    print(mat[i][col])
                    print(i,col)
                    if (mat[i][col]) == 1:
                        
                        colSum += 1
                        print("ColSum: " , colSum)
                if (colSum == 1):
                    res += 1
                
                    
        
        return res
