class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        left,end = 0,0
        ans = []
        for right in range(len(s)):
            end = max(end,dic[s[right]])
            if end == right:
                ans.append(right - left +1)
                left = right + 1
        return ans
        
        