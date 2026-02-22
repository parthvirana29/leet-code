class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freqMap = {}
        result = 0
        seenDouble = False
        for i in words:
            reverse = i[1] + i[0]
            print(reverse)
            if reverse in freqMap:
                if (freqMap[reverse] > 0):
                    freqMap[reverse] -= 1
                    result += 4
                else:
                    # you missed this important!! Add [i] to freqMap if not used
                    freqMap[i] = freqMap.get(i,0) + 1
            
            else:
                freqMap[i] = freqMap.get(i,0) + 1
        for k,v in freqMap.items():
            if k[0] == k[1] and v > 0:
                result += 2
                break

            

        return result
