class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"}":"{","]":"[",")":"("}
        for i in s:
            if i == "(" or i == "[" or  i == "{":
                stack.append(i)
            else:
                if stack and dic[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        