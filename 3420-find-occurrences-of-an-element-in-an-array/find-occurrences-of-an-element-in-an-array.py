class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        res = []
        occurenceMap = {}
        freq = 0
        for i in range(len(nums)):
            if nums[i] == x:
                freq += 1
                occurenceMap[freq] = i
        for query in queries:
            if query > freq:
                res.append(-1)
            elif (query in occurenceMap):
                res.append(occurenceMap[query])
        return res

