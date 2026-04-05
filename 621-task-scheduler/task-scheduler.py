class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        print(counter)
        max_freq = max(counter.values())
        elems_with_max_freq = 0
        for key, val in counter.items():
            
            if val == max_freq:
                elems_with_max_freq += 1
        
        print(max_freq)
        unique_elems = len(counter)
        total_elems = len(tasks)
        print(elems_with_max_freq)
        # a,a,a,b,b,b n = 2, 8 
        # a,c,a,b,d,b n = 1, 6 
        # a,a,a,b,b,b n = 3, 10 


        # A,B,A,B,C,D
        # unique = 4, max_freq = 2, total_elems = 6
        # total - unique = 2
        # which means 2 elements have max_freq = 2
    
        res = max(len(tasks), (max_freq - 1)* (n+1) + elems_with_max_freq)
 
        return res

