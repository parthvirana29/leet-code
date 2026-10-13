class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt_gain = 0
        pre_sum = 0
        for i in range(len(gain)):
            pre_sum += gain[i]
            alt_gain = max(alt_gain, pre_sum)
        return alt_gain