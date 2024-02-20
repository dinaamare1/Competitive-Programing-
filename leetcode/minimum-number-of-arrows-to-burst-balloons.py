class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 1
        points.sort()
        print(points)
        mins = points[0][1]
        for i in range(len(points)):
            if mins>=points[i][0]:
                mins = min(mins,points[i][1])
            else:
                count += 1
                mins = points[i][1]
        return count
        