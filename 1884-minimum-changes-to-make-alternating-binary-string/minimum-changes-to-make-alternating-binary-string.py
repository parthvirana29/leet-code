class Solution:
    def minOperations(self, s: str) -> int:
        count, n = 0, len(s)
        for i in range(n):
            expected = '0' if i % 2 == 0 else '1'
            if s[i] != expected:
                count += 1
        return min(count, n - count)