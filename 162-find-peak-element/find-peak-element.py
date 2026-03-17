class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if (len(nums) <= 1):
            return 0
        nums.append(float('-inf'))
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i

        return 0