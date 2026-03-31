class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(heights))]
        for i in range(len(heights)-1,-1,-1):
            curr = heights[i]
            can_see = 0
            while stack and stack[-1] < curr:
                stack.pop()
                can_see += 1
            
            if stack:
                can_see += 1
            res[i] = can_see
            stack.append(curr)
        return res

