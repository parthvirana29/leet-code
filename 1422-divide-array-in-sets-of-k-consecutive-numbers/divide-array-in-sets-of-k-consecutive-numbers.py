from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if (n % k != 0):
            return False
        freq = Counter(nums)
        sorted_keys = sorted(freq.keys())
        for num in sorted_keys :
            # if frequency is 0 then the number is compeletely used can't be used in another arry of k elements
            if (freq[num] == 0):
                continue
            curr_freq = freq[num]
            for i in range(k):
                # ensure all k consecutive elements of num have the frequency >= freq[num]
                if freq[num+i] < curr_freq:
                    return False
                # use up the element up to current_frequency
                freq[num+i] -= curr_freq


                
        return True
                           