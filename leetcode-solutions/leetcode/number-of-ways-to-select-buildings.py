class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count('0')
        ones = s.count('1')
        total = 0
        one,zero = 0, 0
        for num in s:
            if num == '0':
                total += one * (ones-one)
                zero += 1 
            else:
                total += zero * (zeros-zero)
                one += 1
        return total
        