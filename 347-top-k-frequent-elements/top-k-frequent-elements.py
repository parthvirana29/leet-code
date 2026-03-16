import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to just store the frequencies
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1

        freq_lst = [[] for i in range(len(nums)+1)]

        for key,value in freq.items():
            freq_lst[value].append(key)

        res = []
        for i in range(len(freq_lst)-1,-1,-1):
            for n in freq_lst[i]:
                res.append(n)
                if (len(res) == k):
                    return res
            
        return res



    

