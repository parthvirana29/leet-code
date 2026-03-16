class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for idx, i in enumerate(strs):
            sorted_str = str(sorted(list(i)))
            freq[sorted_str] = freq.get(sorted_str,[])
            freq[sorted_str].append(idx)
        print(freq)
        result = []
        for key, val in freq.items():
            temp = []
            for idx in val:
                temp.append(strs[idx])
            result.append(temp)
        
        return result