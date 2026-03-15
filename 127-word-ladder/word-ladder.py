from collections import defaultdict, deque
from typing import List

# defaultdict ensures the defaults are returned when we call a function and something does not exist
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        
        # pattern → list of words
        # KNOW HOW TO DO PATTERN BASE MATCHING TO FIND IF 2 WORDS DIFFER BY EXACTLY ONE CHARACTER IN THE SAME POSITION.
        # time complexity is O(n*k^2) because n words, each of the n words create k patterns and each pattern costs k
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
               
                pattern_map[pattern].append(word)
        print(pattern_map)

        # now that we have the pattern map how do I use it to find the shortest path to end word?
        
        # add the logic to know exactly which level you are at.
        q = deque([(beginWord, 1)])   # (word, level)
        visited = set([beginWord])
        # THIS IS A LEVEL BY LEVEL BFS (LOOK AT IT IN DEPTH)
        while q:
            word, level = q.popleft()

            if (word == endWord):
                return level
            
            for i in range(L):
                # reconstruct the patterns and get the values
                pattern = word[:i] + '*' + word[i+1:]
             
                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, level+1))
                # putting the pattern map to empty to avoid iterating through the pattern_map even though the words are in visited
                pattern_map[pattern] = []
         
        
        return 0