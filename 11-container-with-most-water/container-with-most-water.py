class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxArea = 0

        while (l < r):
            area = min(height[l], height[r]) * (r - l)
            print(area)
            maxArea = max(maxArea, area)
            if (height[l] < height[r]):
                l += 1
            elif (height[r] < height[l]):
                r -= 1
            else:
                l += 1
                r -= 1
        return maxArea

        # 8, 49, 18, 40, 12, 10, 2