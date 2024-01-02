class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        arr = [0]*(max(costs)+1)
        ans = []
        sums = 0
        count = 0
        for idx,val in enumerate(costs):
            arr[val] += 1
        for idx,val in enumerate(arr):
            ans.extend([idx]*val)
        for i in range(len(ans)):
            sums += ans[i]
            if sums<=coins:
                count += 1
        return count
        