from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        print(freq)
        heap =  [-f for f in list(freq.values())]
        print(heap)
        num_tasks = len(heap)
        heapq.heapify(heap)
        time = 0
        while (heap):
            cycle = n + 1
            temp = []
            tasks_done = 0
        
            while (cycle and heap):
                freq = heapq.heappop(heap)
                cycle -= 1
                tasks_done += 1
                if freq + 1 < 0:
                    temp.append(freq+1)
            
            for t in temp:
                heapq.heappush(heap, t)
            time += n + 1 if heap else tasks_done
        return time 



