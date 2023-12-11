class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        maxs = 0
        for i in arr:
            dic[i] += 1
        for i in dic:
            maxs = max(maxs,dic[i])
        for i in dic:
            if dic[i] == maxs:
                return i
        