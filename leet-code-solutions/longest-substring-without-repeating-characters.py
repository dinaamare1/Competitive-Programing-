class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs = 0
        l = 0
        dic = defaultdict(int)
        for r in range(len(s)):
            dic[s[r]] += 1
            while dic[s[r]]>1:
                dic[s[l]] -= 1
                l += 1
            maxs = max(maxs,r-l+1)
        return maxs