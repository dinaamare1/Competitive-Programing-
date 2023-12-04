class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len (num1) + len(num2)
        ans = [0]*n
        num1, num2 = num1[::-1], num2[::-1]
        if "0" in [num1,num2]:
            return "0"
        for i,a in enumerate(num1):
            for j,b in enumerate(num2):
                value = int(a)*int(b)
                ans[i+j] += value
                ans[i+j+1] += (ans[i+j] // 10)
                ans[i+j] = ans[i+j] % 10
        ans = ans[::-1]
        zeros = 0
        while zeros < len(ans) and ans[zeros] == 0 :
            zeros += 1
        return "".join(map(str,ans[zeros:]))
