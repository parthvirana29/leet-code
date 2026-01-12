class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # take the word if letters are same OR
        # take the word if exact same pair exists
        freq = {}
        palindromeLen = 0
        for i in words:
            freq[i] = freq.get(i, 0) + 1
        usedCenter = False
        for key, value in freq.items():
            opposite = key[1] + key[0]
            if key[0] == key[1]:
                pairs = value // 2
                palindromeLen += pairs * 4
                freq[key] -= pairs * 2
                if (freq[key] > 0 and not usedCenter):
                    freq[key] -= 1
                    palindromeLen += 2
                    usedCenter = True

                continue

            if opposite in freq:
                minCount = min(value, freq[opposite])
                palindromeLen += (min(value, freq[opposite])*4)
                freq[opposite] -= minCount
                freq[key] -= minCount
            print("PalindromeLen: ", palindromeLen)
        
        return palindromeLen

