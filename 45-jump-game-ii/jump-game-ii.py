class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            # in case we were not gauranteed to reach end
            if farthest <= i:
                return -1 
            if i == current_end:
                jumps += 1
                current_end = farthest

            print("i: ", i, "nums[i]: ", nums[i], "current_end: ", current_end, "farthest: ", farthest, "jumps: ", jumps)
                
        
        return jumps