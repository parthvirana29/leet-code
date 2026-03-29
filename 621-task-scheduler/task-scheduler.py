from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Example 1:
        [A, A, A, B, B, B]
        n = 2
        
        A _ _ A _ _ A
        -> [A _ _] [A _ _] [A] -> (max_freq - 1)
        => A _ _ => (n + 1)
        ~> A & B both appear 3 times
        (max_freq - 1) * (n + 1) + num_max = (3 - 1) * (2 + 1) + 2

        Example 2:
        [A, A, A, B, B]
        n = 2
        
        (max_freq - 1) * (n + 1) + num_max = (3 - 1) * (2 + 1) + 1

        Example 3:
        [A, A, A, B, B, B, C, C, D, D]
        n = 2

        A _ _ A _ _ A _ _
        A B _ A B _ A B _
        A B C A B D A B C...
        (max_freq - 1) * (n + 1) + num_max => not enough for all tasks

        so, only len(tasks) will be enough (no idle needed)
        """
        task_count = Counter(tasks).values()
        max_freq = max(task_count)
        num_max = list(task_count).count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)