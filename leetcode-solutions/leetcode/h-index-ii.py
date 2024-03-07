class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = max(citations) + 1
        while left + 1<right:
            mid = (left+right) // 2
            if mid<=len(citations) - bisect_left(citations,mid):
                left = mid
            else:
                right = mid
        return left
                