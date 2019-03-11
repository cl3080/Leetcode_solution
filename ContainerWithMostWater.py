class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        l = 0
        r = size-1
        area = 0
        while l<r:
            w = r-l
            h = min(height[l],height[r])
            area = max(w*h,area) 
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return area
