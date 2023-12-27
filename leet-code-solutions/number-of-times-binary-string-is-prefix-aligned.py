class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxs = 0
        count = 0
        for i in range(len(flips)):
            maxs = max(maxs,flips[i])
            if i+1 == maxs:
                count += 1
        return count
        
        # n = len(flips)
        # strs =[0]*(n+1)
        # count = 0
        # maxs = 0
        # for i in range(len(flips)):
        #     strs[flips[i]] = 1
        #     maxs = max(maxs,flips[i])
        #     sums = sum(strs)
        #     if sums == maxs:
        #         count += 1
        # return count

