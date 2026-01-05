class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # distance = target - position
        # time = distance / speed = m / m/s = m * s/m = s
        # time = ( target - position ) / speed
        # time is the deciding factor bc we are limited by time it takes a car to reach the target

        # it is a stack problem because we need to group items. Stack has to be monotically decreasing. If not then we have found one fleet

        # let's sort the position because a car is only limited if the car ahead is slow
        # combine both position and speed so speed is in correct order:
        combine = zip(position, speed)
        # by default sorts by the first element (position in our case)
        sorted_combine = sorted(combine)

        # now calculate the time stamps for arrival
        timeTaken = []
        for i, j in sorted_combine:
            timeTaken.append((target - i) / j)
        stack = []
        res = 0
        # should be monotonically decreasing stack

        # reverse the timeTaken so we know the arrival time from closest to target to farthest. For ex: 6, 2, 12 so if it's not reversed we will separate [6], [2,12]. However it should be [6,2,12] in one group so knowing the future is important hence reverse timeTaken
        for i in reversed(timeTaken):
            if (stack == []):
                stack.append(i)
            else:
                if (stack[-1] >= i):
                    continue
                res += 1
                stack = [i]
        if (stack != []):
            res += 1
        return res

        # once we have timestamp and position in right order then we can iterate and find the cards that are limited. 
