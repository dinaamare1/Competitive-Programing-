class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        dic1 = Counter(p)
        length = len(p)
        count = Counter(s[:length])
        if count == dic1:
            ans.append(0)
        for i in range(len(s)-length):
            count[s[i]] -= 1
            count[s[i+length]] += 1
            if count == dic1:
                ans.append(i+1)
        return ans
