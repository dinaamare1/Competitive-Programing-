class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = []
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                sub = s[i:j+1]
                for k in sub:
                    if k in sub and k.swapcase() in sub:
                        count += 1
                if count == len(sub):
                    ans.append(sub)
                count = 0
        h = defaultdict(list)
        if not ans:
            return ""
        else:
            for i in ans:
                h[len(i)].append(i)
            maxI = max(list(h.keys()))
            return h[maxI][0]
