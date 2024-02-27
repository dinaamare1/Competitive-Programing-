class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for val in s:
            if val == "(":
                stack.append(ans)
                ans = 0
            else:
                ans = stack.pop() + max(ans * 2, 1)
        return ans