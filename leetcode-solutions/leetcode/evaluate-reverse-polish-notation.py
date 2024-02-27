class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if stack and token == "+":
                val = stack.pop()
                val2 = stack.pop()
                stack.append(val+val2)
            elif stack and token == "/":
                val = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val))
            elif stack and token == "-":
                val = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val)
            elif stack and token == "*":
                val = stack.pop()
                val2 = stack.pop()
                stack.append(val*val2)
            else:
                stack.append(int(token))
        return stack[0]
            
        