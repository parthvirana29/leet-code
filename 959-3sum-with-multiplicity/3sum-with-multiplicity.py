from collections import Counter
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        print(count)
        keys = sorted(count)
        print(keys)
        result = 0
        for i, num in enumerate(keys):
            l,r = i, len(keys) - 1
            complement = target - num
            while (l <= r):
                num2,num3 = keys[l], keys[r]
                if (num2 + num3) < complement:
                    l += 1
                elif (num2 + num3) > complement:
                    r -= 1
                else:
                    if i < l < r:
                        result += count[num] * count[num2] * count[num3]
                    # C(n, 2) = n! / (2! * (n-2)!) = n * (n-1) / 2
                    elif i == l < r:
                        result += (count[num] * (count[num2]-1))//2 * count[num3]
                    elif i < l == r:
                        result += count[num] * (count[num2] * (count[num3] -1))//2
                    else:
                        result += (count[num] * (count[num2] - 1) * (count[num3] - 2))//6
                    l += 1
                    r -= 1
        return result % MOD




