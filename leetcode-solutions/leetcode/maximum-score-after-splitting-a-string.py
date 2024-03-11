class Solution:
    def maxScore(self, s: str) -> int:
        count1 = s.count("1")
        count0 = 0
        maxs = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                count0 += 1
            else:
                count1 -= 1
            maxs = max(maxs,count0+count1)
        return maxs