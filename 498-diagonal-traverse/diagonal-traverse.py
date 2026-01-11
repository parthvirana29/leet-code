class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        res = []

        bottom_bound = len(mat)
        right_bound = len(mat[0])

        x = y = 0
        counter = 0
        going_up = True   # direction flag

        while counter < bottom_bound * right_bound:
            res.append(mat[x][y])
            counter += 1

            if going_up:
                # reached right boundary
                if y == right_bound - 1:
                    x += 1
                    going_up = False
                # reached top boundary
                elif x == 0:
                    y += 1
                    going_up = False
                else:
                    x -= 1
                    y += 1
            else:
                # reached bottom boundary
                if x == bottom_bound - 1:
                    y += 1
                    going_up = True
                # reached left boundary
                elif y == 0:
                    x += 1
                    going_up = True
                else:
                    x += 1
                    y -= 1

        return res
