class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxPointsOnLine = 1

        for i in range(len(points)):
            slopeFreq = {}
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1,len(points)):
                x2, y2 = points[j][0], points[j][1]
                numerator = y2 - y1
                denominator = x2-x1
                if (denominator == 0 ):
                    slope = float('inf')
                else:
                    slope = numerator/denominator


                slopeFreq[slope] = slopeFreq.get(slope, 1) + 1

            # find the maximum value
            for key, val in slopeFreq.items():
                print(key, val)
                maxPointsOnLine = max(maxPointsOnLine, val)
        return maxPointsOnLine



                
