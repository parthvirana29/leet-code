class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # REMEMBER FINDING MAX_AVG IS BASICALLY FINDING MAX_SUM. THE K IS CONSTANT!!!
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum = window_sum -  nums[i-k] + nums[i] 
            max_sum = max(max_sum, window_sum)
        return max_sum / k