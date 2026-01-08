from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        def canEatAll(k):
            return sum(math.ceil(p / k) for p in piles) <= h
        
        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid  # Try to lower speed
            else:
                left = mid + 1  # Increase speed
        
        return left