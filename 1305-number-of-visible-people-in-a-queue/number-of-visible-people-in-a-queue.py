from collections import deque
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0 ]* len(heights)
        print(res)
        stack = []
        # you have to go in reverse because if you go from 0 --> n solution will be O(N^2)
        # What changes when going in reverse? Please explain
        for i in range(len(heights)-1,-1,-1):
            count = 0
            while (stack and stack[-1] < heights[i]):
                stack.pop()
                count += 1
            print("Count: ", count)
            # this is because first taller person is also visible. Let's say heights[i] == stack[-1] then we can't run the while loop. You may think we can change < to <= but what that will do is it will increment the count however it will also pop from stack which is bad. If heights[i] == stack[-1] then we want both values to stay in stack
            if stack:
                count += 1

            res[i] = count
            # so previous member in line can make a decision if it can see the person or not
            stack.append(heights[i])

            
        return res
            

        

            