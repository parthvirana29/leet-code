class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # perform binary search
        left, right = 0, len(nums)
        while (left < right):
            mid = (left + right) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif mid_num < target:
                left = mid + 1
            else:
                right = mid
        return -1