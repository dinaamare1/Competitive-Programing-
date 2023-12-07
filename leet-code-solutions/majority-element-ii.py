class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        ans = []
        for num in nums:
            dic[num] += 1
        for num in dic:
            if dic[num] > len(nums)//3:
                ans.append(num)
        return ans
