import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        neg_stones = [-s for s in stones]
        heapq.heapify(neg_stones)
        print(neg_stones)
        while(len(neg_stones) > 1):
            a = heapq.heappop(neg_stones)
            b = heapq.heappop(neg_stones)
           
            res = -1 * abs(a-b)
            heapq.heappush(neg_stones, res)
        return -1*neg_stones[0]
