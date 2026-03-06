class Solution:
    def minOperations(self, s: str) -> int:
        numChanges = 0
        num2Changes = 1
        arr = list(s)
        arr2 = list(s)
        arr2[0] ='1' if arr[0] == '0' else '0'
        for i in range(1,len(s)):
            if arr[i] == arr[i-1]:
                if (arr[i-1] == '0'):
                    arr[i] = '1'
                else:
                    arr[i] = '0'
                numChanges += 1
            if arr2[i] == arr2[i-1]:
                if (arr2[i-1] == '0'):
                    arr2[i] = '1'
                else:
                    arr2[i] = '0'
                num2Changes += 1
        return min(numChanges, num2Changes)

    
            

            