class Solution:
    def numberOfWays(self, s: str) -> int:
        
        zeros = s.count('0')
        ones = len(s)-zeros 
        total = 0
        prev_one, prev_zero = 0, 0
        for num in s:
            if num == '0':
                total += prev_one * (ones-prev_one)
                prev_zero += 1 
            else:
                total += prev_zero * (zeros-prev_zero)
                prev_one += 1
        return total
        