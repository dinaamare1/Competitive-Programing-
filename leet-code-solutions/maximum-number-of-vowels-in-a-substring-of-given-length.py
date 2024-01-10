class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o','u'}
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowel:
                s[i] = 1
            else:
                s[i] = 0
        maxs = sum(s[:k])
        sums =sum(s[:k])
        for i in range(len(s)-k):
            sums -= s[i]
            sums += s[i+k]
            maxs = max(maxs,sums)
        return maxs

