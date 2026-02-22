class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # freqModMap = {30: 3]}
        freqModMap = {}
        CONST = 60
        result = 0
        for i in range(len(time)):
            mod = time[i] % CONST
            partnerMod = (CONST - mod) % 60
            if partnerMod in freqModMap:
                # do something:
                result += freqModMap[partnerMod]
            
            freqModMap[mod] = freqModMap.get(mod,0) + 1
        return result
            
                
