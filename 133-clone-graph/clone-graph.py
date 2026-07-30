"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            dupe = Node(node.val)
            visited[node] = dupe
            n_dupe_lst = []
            for n in node.neighbors:
                n_dupe_lst.append(dfs(n))
            dupe.neighbors = n_dupe_lst
            return dupe
        return dfs(node)
