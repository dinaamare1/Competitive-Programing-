class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for idx,val in enumerate(path):
            if val == "" or val == ".":
                continue
            if val == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(val)
        return "/"+ "/".join(stack)
        