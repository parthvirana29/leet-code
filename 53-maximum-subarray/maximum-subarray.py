class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pastSum = float('-inf')
        res = pastSum
        for i in range(len(nums)):
            # THIS IS GREEDY TAKES WHATEVER IS BEST AT THIS MOMENT
            pastSum = max(pastSum + nums[i], nums[i])
            # THIS WILL ENSURE THAT ONLY THE MAX VALUE IS KEPT.
            res = max(res, pastSum)
        return res
        