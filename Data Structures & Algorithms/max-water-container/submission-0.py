class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for l in range(len(heights)): 
            r = l + 1
            for r in range(len(heights)):
                curr = min(heights[l],heights[r]) * (r - l)
                if( max_area < curr):
                    max_area = curr 
        return  max_area
