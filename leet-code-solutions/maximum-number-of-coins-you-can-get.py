class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        sums = 0
        i = len(piles)-2
        j = 0
        while j < n:
            sums += piles[i]
            i -= 2
            j+= 1
        return sums