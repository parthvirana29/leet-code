class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seenOne = False
        seen0 = False
        for i in range(len(s)):
            if (s[i] == '1' and not seenOne):
                print("I get in here 1")
                seenOne = True
            elif (s[i] == '0'):
                print("I get in here 2")
                seen0 = True
            else:
                print("I get in here 3")
                if (seenOne & seen0):
                    return False

        return True

