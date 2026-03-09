class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [["" for i in range(len(s))]for j in range(numRows)]
        row, col = 0, 0
        idx = 0
        while (idx < len(s)):
            if (row == 0):
                for i in range(numRows):
                    if (idx >= len(s)):
                        break
                    res[i][col] = s[idx]
                    idx += 1
                row = numRows - 1
                col += 1
            if (row == numRows - 1):
                for i in range(numRows - 2,0,-1):
                    if (idx >= len(s)):
                        break
                    res[i][col] = s[idx]
                    idx += 1
                    col += 1
                row = 0

        zigzag = "".join(ch for row in res for ch in row if ch != "")
        return zigzag



            

