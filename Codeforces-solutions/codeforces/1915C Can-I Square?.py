n = int(input())
from math import sqrt
for _ in range(n):
    x = int(input())
    nums = list(map(int,list(input().split())))
    sums = (sum(nums))
    sqrts = int(sqrt(sums))
    if sqrts*sqrts == sums:
        print("YES")
    else:
        print("NO")