class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dic = {"T":0,"F":0}
        l = 0
        maxs = float("-inf")
        for r in range(len(answerKey)):
            dic[answerKey[r]] += 1
            while dic["T"] > k and dic["F"] >k and l<r:
                dic[answerKey[l]] -= 1
                l += 1
            maxs = max(maxs,r-l+1)
        return maxs