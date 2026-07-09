class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        count = 0
        for i in nums:
            count += i
            res.append(count)

        return res