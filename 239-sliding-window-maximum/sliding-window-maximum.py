from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_stack = deque()
        res = []
        for i in range(len(nums)):
            # remove from stack if out of bounds mono_stack has values < i - k
            while (mono_stack and mono_stack[0] <= i - k):
                mono_stack.popleft()
            while (mono_stack and nums[mono_stack[-1]] < nums[i]):
                mono_stack.pop()
            mono_stack.append(i)
            if i >= k - 1:
                res.append(nums[mono_stack[0]])
        return res