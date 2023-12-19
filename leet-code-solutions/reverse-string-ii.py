class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            p1 = i
            p2 = min(p1 + k - 1, len(s) - 1) 
            while p1 < p2:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
        return ''.join(s)