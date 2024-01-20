class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        nums.insert(0,0)
        ans = []
        n = len(nums)
        pre = 0
        for i in range(1,n):
            pre+=nums[i]
            prefix.append(pre)
        for i in range(1,len(prefix)):
            val1 = abs(prefix[i-1]-(nums[i]*(i-1)))
            val2 = abs(abs(prefix[n-1] - prefix[i-1]) - (nums[i]*(n-i)))
            ans.append(val1+val2)
        return ans
        