class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        limit = truckSize
        units_taken = 0
        for  num_boxes, num_units in boxTypes:
            if (limit == 0):
                break
            units_taken += (min(limit, num_boxes)*num_units)
            limit -= min(limit, num_boxes)
        return units_taken
            