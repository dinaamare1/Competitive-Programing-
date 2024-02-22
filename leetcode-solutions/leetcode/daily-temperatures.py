class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for idx,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                x = stack.pop()
                ans[x] = idx - x
            if stack and temperatures[stack[-1]] > temp:
                stack.append(idx)
            else:
                stack.append(idx)
        return ans



        