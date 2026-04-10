from collections import deque, defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        # 3 - 1, 5, 10
        pmap = defaultdict(list)
        for i in range(len(ppid)):
            pmap[ppid[i]].append(pid[i])
        print(pmap)
        q = deque([kill])
        result = []
        while q:
            killed = q.popleft()
            result.append(killed)
            if killed in pmap:
                for neighbor in pmap[killed]:
                    q.append(neighbor)
        return result



