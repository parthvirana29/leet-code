class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertSet = [set() for i in range(9)]
        horSet = [set() for i in range(9)]
        boxSet = [set() for i in range(9)]
        rows = 9
        cols = 9
        for i in range(rows):
            for j in range(cols):
                # check horizontal
                if board[i][j] != '.': 
                    num = board[i][j]
                    if  num  in horSet[i]:
                        return False
                    horSet[i].add(num)
                    
                    # check Vertical
                    if num in vertSet[j]:
                        return False
                    vertSet[j].add(num)
                    
                    # check 3by3

                    boxNum = (i // 3) * 3 + (j//3)
                    if num in boxSet[boxNum]:
                        return False
                    boxSet[boxNum].add(num)
        return True
            
