from collections import deque
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Initialize result list with zeros
        res = [0] * len(heights)
        stack = []  # Monotonic stack: stores heights of people to the right

        # Iterate from right to left.
        # Why reverse? Because we want to know for each person how many people
        # to their right are visible. If we iterate left → right, we would need
        # to scan all people to the right every time → O(n^2). By going in reverse,
        # the stack already contains the "future" right-side people in decreasing order,
        # so we can determine visibility in O(n) amortized.
        for i in range(len(heights) - 1, -1, -1):
            count = 0

            # Pop all shorter people from the stack.
            # They are fully visible to the current person.
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1

            # If stack is not empty, the first taller or equal person is also visible
            # but we do NOT pop them, because they may block visibility for people to the left.
            # Important: We cannot change < to <= because that would remove a person of equal height,
            # which breaks the stack invariant for future iterations.
            if stack:
                count += 1

            # Store the count of visible people for current index
            res[i] = count

            # Push the current person's height onto the stack.
            # This height may block visibility for the next person to the left.
            stack.append(heights[i])

        return res