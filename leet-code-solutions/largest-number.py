class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = [str(num) for num in nums]
        ans.sort(reverse=True)
        for i in range(len(ans)):
            for j in range(len(ans)-1):
                if int(ans[j+1]+ans[j]) > int(ans[j] + ans[j+1]):
                    ans[j+1],ans[j] = ans[j],ans[j+1]
        return str(int("".join(ans)))