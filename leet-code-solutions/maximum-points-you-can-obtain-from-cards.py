class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        maxs = sum(cardPoints[len(cardPoints)-k:])
        sums = sum(cardPoints[len(cardPoints)-k:])
        x = len(cardPoints)-k
        for r in range(x,len(cardPoints)):
            sums += cardPoints[l]
            sums -= cardPoints[r]
            l += 1
            maxs = max(maxs,sums)
        return maxs



            