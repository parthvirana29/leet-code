import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to just store the frequencies
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        print(freq)
        freq_lst = [[] for i in range(len(nums))]
        print(freq_lst)
        for key,value in freq.items():
            freq_lst[value-1].append(key)
        res = []
        print(freq_lst)
        for i in range(len(freq_lst)-1,-1,-1):
            if freq_lst[i] != []:
                print("I get in here")
                j = len(freq_lst[i])
                while (j > 0  and k > 0):
                    res.append(freq_lst[i][j-1])
                    print("res: ", res)
                    k -= 1
                    j -= 1
        return res



    

