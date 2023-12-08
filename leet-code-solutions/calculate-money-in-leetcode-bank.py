class Solution:
    def totalMoney(self, n: int) -> int:
        days=1
        temp=0
        sums=0
        for i in range(n):
            if i%7 == 0:
                days = 1 + temp
                temp += 1
            sums +=  days
            days += 1
        return sums
            