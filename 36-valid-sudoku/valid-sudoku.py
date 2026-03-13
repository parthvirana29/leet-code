class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkHorizontal(board):
            for i in range(len(board)):
                uniqueSet = set()
                for j in range(len(board[0])):
                    if board[i][j] != "." and board[i][j] in uniqueSet:
                        return False
                    uniqueSet.add(board[i][j])
                # print("Horizontal Unique set: ", uniqueSet)
            return True
        
        def checkVertical(board):
            for i in range(len(board)):
                uniqueSet = set()
                for j in range(len(board[0])):
                    if board[j][i] != "." and board[j][i] in uniqueSet:
                        return False
                    uniqueSet.add(board[j][i])
                # print("Vertical Unique Set: ", uniqueSet)
            return True


        def check3By3(board):
            startX = 0
            startY = 0
            for vert in range(3):
                startX = 0
                for h in range(3):
                    uniqueSet = set()
                    for i in range(startY, startY + 3):
                        for j in range(startX, startX + 3):
                            print(i,j)
                            if board[i][j] != "." and board[i][j] in uniqueSet:
                                
                                return False
                            uniqueSet.add(board[i][j])
                    print("_________________________")
                    startX += 3
                startY += 3
            return True
        return checkHorizontal(board) and checkVertical(board) and check3By3(board)

