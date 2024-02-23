class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic= Counter(s)
        stack = []
        for val in s:
            if val in stack:
                dic[val] -= 1
                continue 
            while stack and stack[-1] > val and dic[stack[-1]]>1:
                x = stack.pop()
                dic[x] -= 1
            stack.append(val)
        return "".join(stack)

        