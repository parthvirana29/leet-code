import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # start                target
        # sttations = [] t = 1 startFuel = 1 res = 0 b/c we can reach target without refueling
        # fuel = 60 - 10 - 10 - 30
        # [30, 30]
        if (startFuel == target):
            return 0
        if (stations and startFuel < stations[0][0]):
            return -1
        stations.append([target,0])
        fuel_in_tank = startFuel
        prev_pos = 0
        heap = []
        num_stops = 0

        for i in range(len(stations)):
            cur_pos, cur_fuel = stations[i]
            # update the fuel tank
            distance_travelled = cur_pos - prev_pos
            fuel_in_tank -= distance_travelled


            while (heap and fuel_in_tank < 0):
                # we need fuel
                fuel_avail = heapq.heappop(heap)
                fuel_in_tank += (-1*fuel_avail)
                # increment num_stops
                num_stops += 1
            if (fuel_in_tank < 0):
                return -1
                

            heapq.heappush(heap, -1*cur_fuel)


            prev_pos = cur_pos
        return num_stops


        