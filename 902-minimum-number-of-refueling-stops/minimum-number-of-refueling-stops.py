import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []          # will store fuels as negative for max heap
        fuel = startFuel
        prev = 0
        stops = 0
        
        stations.append([target, 0])   # handle final stretch
        
        for pos, cap in stations:
            fuel -= (pos - prev)       # distance from last point
            
            # refuel when forced
            while max_heap and fuel < 0:
                fuel += -heapq.heappop(max_heap)
                stops += 1
            
            if fuel < 0:
                return -1
            
            heapq.heappush(max_heap, -cap)
            prev = pos
        
        return stops