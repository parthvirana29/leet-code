class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # idxModMap = {30: [0,1,3]} value is a list with indices
        idxModMap = {}
        CONST = 60
        result = 0
        for i in range(len(time)):
            mod = time[i] % CONST
            partnerMod = (CONST - mod) % 60
            if partnerMod in idxModMap:
                # do something:
                result += len(idxModMap[partnerMod])
            if (mod in idxModMap):
                idxModMap[mod].append(i)
            else:
                idxModMap[mod] = [i]
        return result
            
                
