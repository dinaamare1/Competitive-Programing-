class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxs = float("-inf")
        for i in range(len(points)-1):
            diff = abs(points[i][0] - points[i+1][0])
            maxs = max(maxs,diff) 
        return maxs