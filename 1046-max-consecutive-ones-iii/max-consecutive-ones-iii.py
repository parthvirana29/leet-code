class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        localK = k
        maxLen = 0
        for r in range(len(nums)):
            if (nums[r] == 1):
                maxLen = max(maxLen, r - l + 1)

            elif (nums[r] == 0 and localK > 0):
                localK -= 1
                maxLen = max(maxLen, r - l + 1)
                
            else:
                maxLen = max(maxLen, r - l)
               
                while(localK == 0):
                    if (nums[l] == 0):
                        localK += 1
                      
                    l += 1
                # VERY VERY VERY IMPORTANT. Decrement localK to account for 0 you just found!!!! So at the end localK = 0 but l is shifted.
                localK -= 1
                

        
        return maxLen

