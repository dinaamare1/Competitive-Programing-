class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        newIntervals = []
        for i in range(len(intervals)):
            newIntervals.append((intervals[i][0],i))
        newIntervals.sort()
        def checker(val):
            left = -1
            right = len(intervals)
            curr = -1
            while left + 1< right:
                mid = (left+right)//2
                if newIntervals[mid][0] >= val:
                    right = mid
                    curr = newIntervals[mid][1]
                else:
                    left = mid
            return curr

    
        for first,second in intervals:
            ans.append(checker(second))
    
        return ans