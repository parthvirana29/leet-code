class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setList = set(nums)
        maxLen = 0
        # find the start:
        startList = []
        for i in setList:
            if i - 1 not in setList:
                startList.append(i)
        for ps in startList:
            curr = 0
            while (ps in setList):
                curr += 1
                ps += 1
            maxLen = max(maxLen, curr)
        return maxLen


