class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # u can't sort
        # if I have to optimize on time then trade of is the space
        # now thinking of a data structure to store it in a manner I can find the consecutive sequence
        # the only data structure with constant O(1) insertion would be hash map / sets
        # I didn't know how to move forward so I took a look at neetcode.io's hints section for this problem
        # HARDEST PART: breaking the problem down into to steps: finding start, and using the start to find the sequence.
        # it suggested I create a set so I created a set to get rid of duplicates
        numsSet = set(nums)
        possibleStart = []
        longestSeq = 0
        # another hint it gave was to find the start of seq. A number can be considered start of seq if and only if the prev number does not exist.
        for i in numsSet:
            if i-1 not in numsSet:
                possibleStart.append(i)
        # once I had possibleStart I iterate through them and calculate the consecutive sequence for each possible start. Store the longest sequence found and return it.
        for i in possibleStart:
            start = i
            while start + 1 in numsSet:
                start += 1
            longestSeq = max(longestSeq, start - i + 1)
        return longestSeq


                

