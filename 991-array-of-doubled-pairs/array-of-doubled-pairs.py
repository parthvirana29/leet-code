class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        # Sort by absolute value
        for x in sorted(freq.keys(), key=abs):
            if freq[x] == 0:
                continue

            if freq.get(2 * x, 0) < freq[x]:
                return False

            freq[2 * x] -= freq[x]

        return True
