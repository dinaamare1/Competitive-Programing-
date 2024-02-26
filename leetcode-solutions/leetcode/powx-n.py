class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n == 0:
                return 1
            if n % 2:
                return  x * power((x*x),(n-1)//2)
            else:
                return power((x*x),n//2)
        if n < 1:
            return 1 / power(x,abs(n))
        elif n == 0:
            return 1
        else:
            return power(x,abs(n))
        