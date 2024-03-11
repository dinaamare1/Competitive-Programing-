class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        left = 0
        k = len(s)// 4
        mins = float("inf")

        def check():
            return count["Q"] <= k and count["W"] <= k and count["E"] <= k and count["R"] <= k
        for right in range(len(s)):
            count[s[right]] -= 1
            while left < len(s) and check():
                mins = min(mins,right-left+1)
                count[s[left]] += 1
                left += 1
        return mins

        
