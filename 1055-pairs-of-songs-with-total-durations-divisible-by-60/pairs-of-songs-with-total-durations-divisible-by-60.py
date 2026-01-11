class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # i tried using set previously but in that case I lost the occurences of each value. Hence creating frequency map
        res = 0
        freq = {}
        CONST = 60
        for i in time:
            modI = i % 60
            complement = abs(CONST - modI)%60
            # storing remainders because any number with complement remainder will be a multiple of 60
            if complement in freq:
                res += freq[complement]
            
            freq[modI] = freq.get(modI,0) + 1
        return res
            
            
            
            

        