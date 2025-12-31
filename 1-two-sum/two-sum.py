class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = set()
        for i in range(len(nums)):
            comp = target - nums[i]
            if (comp in compliments):
                return [nums.index(comp), i]
            else:
                compliments.add(nums[i])
        return []