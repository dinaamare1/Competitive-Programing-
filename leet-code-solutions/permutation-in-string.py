class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = Counter(s1)
        k =len(s1)
        dic1 = Counter(s2[:k])
        if dic == dic1:
            return True
        for i in range(len(s2)-k):
            if s2[i] in dic1:
                dic1[s2[i]] -= 1
                if dic1[s2[i]] == 0:
                    del dic1[s2[i]]
            dic1[s2[i+k]] += 1
            if dic1 == dic:
                return True
        return False
        