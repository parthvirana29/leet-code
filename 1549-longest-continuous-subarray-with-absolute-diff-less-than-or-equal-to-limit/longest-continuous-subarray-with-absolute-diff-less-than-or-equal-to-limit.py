from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxSubLen = 0
        maxdq = deque()
        mindq = deque()
        maxdq2 = deque()
        mindq2 = deque()
        
        l = 0
        for r in range(len(nums)):
            while (maxdq and nums[maxdq[-1]] < nums[r]):
                maxdq.pop()
                maxdq2.pop()
            maxdq.append(r)
            maxdq2.append(nums[r])

            while (mindq and nums[mindq[-1]] > nums[r]):
                mindq.pop()
                mindq2.pop()
            mindq.append(r)
            mindq2.append(nums[r])

            while (abs(nums[maxdq[0]] - nums[mindq[0]]) > limit):
                l += 1
                if (maxdq[0] < l):
                    maxdq.popleft()
                if (mindq[0] < l):
                    mindq.popleft()
            # print("MAX: " , list(maxdq2))
            # print("MIN: " , list(mindq2))
            maxSubLen = max(maxSubLen, r - l + 1)
        return maxSubLen





        