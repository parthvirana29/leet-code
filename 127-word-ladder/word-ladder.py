from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        
        # pattern → list of words
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)
        
        q = deque([(beginWord, 1)])   # (word, level)
        visited = set([beginWord])
        
        while q:
            word, level = q.popleft()
            
            if word == endWord:
                return level
            
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                
                for nei in pattern_map[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, level + 1))
                
                pattern_map[pattern] = []   # ⭐ avoid reprocessing
        
        return 0