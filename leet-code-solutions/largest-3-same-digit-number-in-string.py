class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxs = 0
        ans = ""
        for i in range(len(num)):
            val = ""
            if i+2<len(num) and num[i] == num[i + 1] == num[i + 2]:
                val+= num[i] * 3
                if val > ans:
                    ans = val
                # maxs = max(maxs,int(val))
                # if maxs == 0:
                #     ans = "000"
                # else:
                #     ans = maxs
        return str(ans)