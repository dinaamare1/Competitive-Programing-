class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                strs = ""
                while stack[-1] != "[":
                    strs = stack.pop() + strs
                stack.pop()
                
                mul = ""
                while stack and stack[-1].isdigit():
                    mul = stack.pop() + mul
                stack.append(int(mul) * strs)
        
        return "".join(stack)
