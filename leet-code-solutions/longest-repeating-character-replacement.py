class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        l = 0
        maxs = float("-inf")
        for r in range(len(s)):
            dic[s[r]] += 1
            val = max(dic.values())
            while r - l + 1 - val>k:
                dic[s[l]]-= 1
                l+= 1
            maxs = max(maxs,r-l+1)
        return maxs

        