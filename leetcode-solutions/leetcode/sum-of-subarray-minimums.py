class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1]
        sums = 0
        arr.append(0)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                val = stack.pop()
                left = val - stack[-1]
                right = i -val
                sums += left*right*arr[val]
            stack.append(i)
        return sums%(10**9 + 7)

