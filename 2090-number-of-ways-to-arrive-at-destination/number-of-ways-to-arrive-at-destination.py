import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v,time])
            graph[v].append([u,time])
        print(graph)
        opt_times = [float('inf')] * n
        ways = [1] * n
        pq = [[0,0]] # time, u
        while (pq):
            u_time,u = heapq.heappop(pq)
            if opt_times[u] < u_time:
                continue
            for v, v_time in graph[u]:
                if opt_times[v] > u_time + v_time:
                    opt_times[v] = u_time + v_time
                    ways[v] = ways[u]
                    heapq.heappush(pq, [opt_times[v], v])
                # this logic is very important if you don;t have this then if one node can reach from two different parent nodes then we will miss another way the v node is reached. IMPORTANT!!!!!!
                elif opt_times[v] == u_time + v_time:
                    ways[v] += ways[u]
        return ways[n-1] % (10**9 + 7)

