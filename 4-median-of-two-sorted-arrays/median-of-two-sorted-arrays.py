import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(log(min(n,m))) because we are running binary search on the minimum of the two
        A, B = nums1, nums2
        if (len(nums2) < len(nums1)):
            A = nums2
            B = nums1
        totalLen = len(A) + len(B)
        half = totalLen // 2
        l, r = -1, len(A) - 1
        mid = 0
        while (l <= r):
            mid = (l+r)//2
            mid_b = half - mid - 2
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid+1] if (mid + 1) < len(A) else float('inf')
            Bleft = B[mid_b] if mid_b >= 0 else float('-inf')
            Bright = B[mid_b + 1] if (mid_b + 1) < len(B) else float('inf')
            if (Aleft <= Bright and Bleft <= Aright):
                if (totalLen%2):
             
                    return min(Aright,Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1
        return -1


        #         break
        #     elif (B[b_partition] > A[a_partitiaion+1]):
        #         l = mid + 1
        #     else:
        #         r = mid
        #         # yay we found partition
        # 1, 2, 3, 4, 5
        # leftPartitionLen = half
        # rightPartitionLen = totalLen - half
        # if (totalLen % 2 != 0):
        #     return B[half+1]
        # return (A[mid] + B[half-mid])//2


