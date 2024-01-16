class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxs = 0
        l = 0
        dic =  defaultdict(int)
        for r in range(len(fruits)):
            dic[fruits[r]] += 1
            while len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    del dic[fruits[l]]
                l += 1
            maxs = max(maxs,r-l+1)
        return maxs