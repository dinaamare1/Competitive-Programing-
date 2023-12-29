class Solution:
    def sortSentence(self, s: str) -> str:
        strs = s.split()
        ans = [""]*(len(strs)+1)
        for val in strs:
            ans[int(val[-1])] = val[:len(val)-1]
        return " ".join(ans[1:])
        