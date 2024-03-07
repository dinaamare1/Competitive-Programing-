# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        if guess(n) == 0:
            return n
        elif guess(1) == 0:
            return 1
        while left<=right:
            mid = (left+right) // 2
            val = guess(mid)
            if val == 0:
                return mid
            elif val == 1:
                left = mid+1
            elif val == -1:
                right = mid -1
        