import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        stops = 0
        fuel = startFuel
        prev = 0 # keeping track of previous to know how much distance i travelled from i-1 to i to see how much fuel i burned
        # this ensures we reach the target and since we use prev, we consider all the edge cases.
        stations.append([target,0])
        for i in range(len(stations)):
            pos, fuel_cap = stations[i][0], stations[i][1]
            fuel -= (pos - prev)
            while (max_heap and fuel < 0):
                # pushing negative fuel_cap because heapq in Python implements min heap by default. Hence keeping - value so max fuel_cap will still be at top of heap
                fuel +=  - heapq.heappop(max_heap)
                stops += 1
            if (fuel < 0):

                return -1
            heapq.heappush(max_heap, -fuel_cap)



            prev = pos
        return stops