n = int(input())
from collections import defaultdict
for _ in range(n):
    x = int(input())
    nums = list(map(str,input()))
    count = defaultdict(int)
    count[0] += 1
    val = 0
    ans = 0
    for i in range(x):
        val += int(nums[i]) - 1
        ans += count[val]
        count[val] += 1
    print(ans)