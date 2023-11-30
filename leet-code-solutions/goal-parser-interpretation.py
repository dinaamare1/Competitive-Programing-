class Solution:
    def interpret(self, command: str) -> str:
        ans = ""

        for i in range(len(command)):
            if command[i] == "(" and command[i+1] == ")":
                ans += "o"
            if command[i] == "(" and command[i+1] == "a":
                ans+= "al"
            if command[i] == "G":
                ans += "G"
        return ans

