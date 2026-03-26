import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in range(len(points)):
            ed = sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(heap, (ed, i))
    
        while (k):
            ed, idx = heapq.heappop(heap)
            res.append(points[idx])
            k -= 1
        return res