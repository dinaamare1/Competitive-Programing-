class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        odd = 0
        res = 0
        for val in count.values():
            if val % 2:
                odd = 1
                res += val - 1
            else:
                res += val
        return res + odd
            
        