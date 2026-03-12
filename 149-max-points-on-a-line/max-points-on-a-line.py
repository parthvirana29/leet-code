class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # initialize the maxPointsOnLine with 1 because constraint mentions 1 <= points.length <= 300
        maxPointsOnLine = 1
        # get the slope w.r.t each of the points
        for i in range(len(points)):
            # generate fresh frequency for each slope w.r.t the curent point
            slopeFreq = {}
            x1, y1 = points[i][0], points[i][1]
            # calculate the slope and update the slope freq
            for j in range(i+1,len(points)):
                x2, y2 = points[j][0], points[j][1]
                numerator = y2 - y1
                denominator = x2-x1
                # division by 0 is impossible
                if (denominator == 0 ):
                    slope = float('inf')
                else:
                    slope = numerator/denominator

                # we are updating the slope freq with base value 1, because 2 points make up a slope
                slopeFreq[slope] = slopeFreq.get(slope, 1) + 1

            # find the maximum occurence for the slope w.r.t current point: points[i]
            for key, val in slopeFreq.items():
                maxPointsOnLine = max(maxPointsOnLine, val)
        # return the maximum occurence of a slope
        return maxPointsOnLine



                
