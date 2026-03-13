class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        # for each idx check if you have reached it or you're behind it.
        for i in range(len(nums)):
            # return false if your max reach is less than current idx. you're behind.
            if (max_reach < i):
                return False
            # take the biggest step you can from a given index. 
            max_reach = max(max_reach, i + nums[i])
        return True
