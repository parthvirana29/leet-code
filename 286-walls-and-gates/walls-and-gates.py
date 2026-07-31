from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # logic is calculate distance wrt each gate and do it for all the gates minimizing the distance at each grid [i][j]
        


        # find all the gates
        gates = []
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append(([i,j], 0))
        print(gates)

        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        q = deque(gates)
        visited = [[0 for i in range(len(rooms[0]))] for j in range(len(rooms))]
        print(q)
        while (q):
            coord, step = q.popleft()
            curr_row, curr_col = coord
            for dr, dc in directions:
                nr, nc = curr_row + dr, curr_col + dc
                if 0 <= nr < len(rooms) and 0 <= nc < len(rooms[0]) and visited[nr][nc] != 1:

                # check if current is gate
                
                    if (rooms[nr][nc] == -1):
                        # we can continue cuz
                        continue
                    else:
                        rooms[nr][nc] = min(rooms[nr][nc], step + 1)
                    q.append(((nr,nc), rooms[nr][nc]))
                    visited[nr][nc] = 1
        return rooms
                    

