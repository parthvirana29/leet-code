class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        intervals.sort(key=lambda x: x[0])
        mergedIntervals = [intervals[0]]
        print(intervals)
        for i in range(1,len(intervals)):
            if (mergedIntervals[-1][0] <= intervals[i][0] <= mergedIntervals[-1][1]):
                mergedIntervals[-1][1] = max(intervals[i][1], mergedIntervals[-1][1])
            else:
                mergedIntervals.append(intervals[i])
        return mergedIntervals

            