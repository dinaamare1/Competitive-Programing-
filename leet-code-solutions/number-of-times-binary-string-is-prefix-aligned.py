class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxs = 0
        count = 0
        for i in range(len(flips)):
            maxs = max(maxs,flips[i])
            if i+1 == maxs:
                count += 1
        return count

