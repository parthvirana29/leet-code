from collections import deque
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        print(start)
        print(end)
        s_pt = e_pt = 0
        # 0, 5, 15
        # 15, 20, 30
        # num_rooms = 1
        # 2, 7
        # 4, 10
        e_pt = 0
        while (s_pt < len(intervals)):
            if start[s_pt] >= end[e_pt]:
                e_pt += 1
            s_pt += 1
        return s_pt - e_pt
            

            
        