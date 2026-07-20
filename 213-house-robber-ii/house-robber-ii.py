class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        house1, house2 = 0, 0
        res1, res2 = 0, 0
        # skip first element
        for i in range(1, len(nums)):
            temp = max(nums[i] + house1, house2)
            house1 = house2
            house2 = temp
        # remove last element
        res1 = house2
        nums.pop()
        house1, house2 = 0, 0
        for i in range(len(nums)):
            temp = max(nums[i] + house1, house2)
            house1 = house2
            house2 = temp

        res2 = house2

        return max(res1, res2)





