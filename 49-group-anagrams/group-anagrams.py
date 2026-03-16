class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for idx, i in enumerate(strs):
            sorted_str =  "".join(sorted(i))
            freq[sorted_str] = freq.get(sorted_str,[])
            freq[sorted_str].append(i)
       
        return list(freq.values())