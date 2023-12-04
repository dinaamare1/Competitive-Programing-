class Solution:
    def printVertically(self, s: str) -> List[str]:
        splited = s.split()
        maxs = float("-inf")
        ans = []
        for word in splited:
            maxs = max(maxs,len(word))
        for i in range(maxs):
            value =[]
            for word in splited:
                if i< len(word):
                    value.append(word[i])
                else:
                    value.append(" ")
            ans.append("".join(value).rstrip())
        return ans