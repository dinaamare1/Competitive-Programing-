class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = set()
        for zero, one in ranges:
            ans |= set(range(zero,one+1))
        return all(val in ans for val in range(left,right+1))
