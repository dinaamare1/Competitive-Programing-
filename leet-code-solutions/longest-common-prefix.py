class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans = ""
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            else:
                ans += strs[-1][i]
        return ans
