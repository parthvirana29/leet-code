class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) <= 1):
            return len(s)
        seenChars = set()
        l = 0
        longestSubstr = 0
        for r in range(len(s)):
            if (s[r] in seenChars):
                # write logic to move the left pointer
                # DO NOT CALCULATE IT HERE LIKE YOU DID PREVIOUSLY BECAUSE WE HAVE TO REMOVE TO GET TO THE RIGHT L.
                while (s[r] in seenChars):
                    seenChars.remove(s[l])
                    l += 1
            seenChars.add(s[r])
            # calculate length of longestSubstring at the end of all the updates
            longestSubstr = max(longestSubstr, r - l + 1 )
        return longestSubstr



