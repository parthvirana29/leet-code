class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # u can't sort
        # if I have to optimize on time then trade of is the space
        # now thinking of a data structure to store it in a manner I can find the consecutive sequence
        # the only data structure with constant O(1) insertion would be hash map / sets
        # I didn't know how to move forward so I took a look at neetcode.io's hints section for this problem
        # it suggested I create a set
        possibleStart = []
        longestSeq = 0
        numsSet = set(nums)
        for i in numsSet:
            if i-1 not in numsSet:
                possibleStart.append(i)
        
        for i in possibleStart:
            start = i
            while start + 1 in numsSet:
                start += 1
            longestSeq = max(longestSeq, start - i + 1)
        return longestSeq


                

