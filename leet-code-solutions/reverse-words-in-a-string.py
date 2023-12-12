class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = []
        for val in s[::-1]:
            if val != " ":
                ans.append(val.strip())
        return " ".join(ans)