class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        upper = x
        def sqr(n):
            return n*n
        while low<=upper:
            mid = (low + upper) // 2
            val = sqr(mid)
            if val>x:
                upper = mid - 1
            else:
                low = mid + 1
        return upper
        