class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        curr = 0
        totalSpace = len(mat) * len(mat[0])
        rowLen = totalSpace / r
        if (r * c != totalSpace ):
            return mat
        xLen = len(mat[0])
        yLen = len(mat)
        res = []
       
        totalSpace = len(mat) * len(mat[0])
        
        while (curr < totalSpace):
            temp = 0
            curRow = []
            while (temp < rowLen):
                x = curr % xLen
                y = (curr // xLen) % yLen
                curRow.append(mat[y][x])
                curr += 1
                temp += 1
            res.append(curRow)
        return res
        
