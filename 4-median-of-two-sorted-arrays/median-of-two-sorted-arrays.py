class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Make A the smaller array
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        
        # mid represents COUNT of elements from A in left partition
        l, r = 0, len(A)  # Can take 0 to len(A) elements from A
        
        while l <= r:
            mid = (l + r) // 2  # Elements from A in left partition
            mid_b = half - mid   # Elements from B in left partition
            
            # Get boundary elements
            # If taking 'mid' elements from A, last one is A[mid-1], first excluded is A[mid]
            Aleft = A[mid - 1] if mid > 0 else float('-inf')
            Aright = A[mid] if mid < len(A) else float('inf')
            
            # Same for B
            Bleft = B[mid_b - 1] if mid_b > 0 else float('-inf')
            Bright = B[mid_b] if mid_b < len(B) else float('inf')
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Found correct partition!
                if total % 2:  # Odd
                    return min(Aright, Bright)
                else:  # Even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                # Too many from A
                r = mid - 1
            else:
                # Too few from A
                l = mid + 1
        
        return -1