from collections import deque
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        print(intervals)
        stack = [intervals[0][1]]
        num_rooms = 1
        for i in range(1,len(intervals)):
            prev_end_time = stack[0]
            curr_start_time = intervals[i][0]
            # 3-30, 15-40, 32-35, 
            if (prev_end_time > curr_start_time ):
                num_rooms += 1
            else:
                heappop(stack)

            heapq.heappush(stack, intervals[i][1])
        return num_rooms

        