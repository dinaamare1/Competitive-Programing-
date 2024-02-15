class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # dic= {}
        # count = 0
        # ans = 0
        # for i in range(len(nums)):
        #     if nums[i] in dic:
        #         if dic[nums[i]] < i:
        #             count += dic[nums[i]]
        #     dic[nums[i]] = i
        # return count
        nums = sorted(nums)
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
