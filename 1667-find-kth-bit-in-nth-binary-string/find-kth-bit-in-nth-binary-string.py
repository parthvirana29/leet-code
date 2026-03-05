class Solution:
    def invert(self, string):
        res = ''
        for i in range(len(string)):
            if string[i] == '0':
                res += '1'
            else:
                res += '0'
        return res

    def findKthBit(self, n: int, k: int) -> str:
        string = '0'
        prev = '0'
        for i in range(1,n):
            prev = string
            string =  prev + '1' + self.invert(prev)[::-1]


        return string[k-1]
