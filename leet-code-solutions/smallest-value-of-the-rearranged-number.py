class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            ans = sorted(list(str(num)))
            if ans[0] == "0":
                for i in range(1,len(ans)):
                    if ans[i] != "0":
                        ans[i],ans[0] = ans[0],ans[i]
                        break
            print(ans)
            return int("".join(ans))
        else:
            ans = sorted(list(str(num*-1)),reverse=True)
            return (int("".join(ans)))*-1