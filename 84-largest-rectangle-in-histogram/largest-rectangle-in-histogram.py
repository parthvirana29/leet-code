class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        max_area = 0
        mono_stack = []
        for i in range(len(heights)):
            # increasing mono_stack
            while (mono_stack and heights[mono_stack[-1]] > heights[i]):
                height_idx = mono_stack.pop()
                height = heights[height_idx]

                width = i if not mono_stack else i - mono_stack[-1] - 1
                max_area = max(max_area, height*width)
            mono_stack.append(i)

        while (mono_stack):
            height_idx = mono_stack.pop()
            height = heights[height_idx]
            # the width is the difference between current idx and the last un popped bar. Why? Because it is the difference between two shorter bars gauranteeing the bars in middle have greater height than the two ends
            width = len(heights) if not mono_stack else len(heights) - mono_stack[-1] - 1
            max_area = max(max_area, height*width)


        return max_area
