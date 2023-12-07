class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        p1 = 0
        for i in range(len(s)):
            if i == spaces[p1]:
                ans.append(" ")
                ans.append(s[i])
                if p1+1 < len(spaces):
                    p1 += 1
            else:
                ans.append(s[i])
        return "".join(ans)


        # this caused a TLE
        # for i in range(len(spaces)):
        #     if i-1>= 0:
        #         ans.append(s[spaces[i-1]:spaces[i]])
        #     else:
        #         ans.append(s[:spaces[i]])
        #     if i + 1 == len(spaces):
        #         ans.append(s[spaces[i]:]) 
        #     print(ans)
        # return " ".join(ans)
        