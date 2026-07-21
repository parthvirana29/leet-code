class Solution:
    def longestPalindrome(self, s: str):

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True
        # check all substrings length from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    continue
                if length <= 3:
                    dp[i][j] = True
                elif dp[i+1][j-1]:
                    dp[i][j] = True
                
                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length
            
        return s[start: start+ max_len]