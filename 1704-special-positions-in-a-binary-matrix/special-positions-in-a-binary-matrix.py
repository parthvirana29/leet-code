class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        for row in range(len(mat)):
            if sum(mat[row]) == 1:
                col = mat[row].index(1)
                colSum = 0
                for i in range(len(mat)):
                  
                    if (mat[i][col]) == 1:
                        
                        colSum += 1
                if (colSum == 1):
                    res += 1
                
                    
        
        return res
