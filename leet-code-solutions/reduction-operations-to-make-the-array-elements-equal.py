class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dic = Counter(sorted(nums))
        count = 0
        for idx,val in enumerate(dic):
            count += idx*dic[val]
        return count





        # count = 0
        # num = nums
        # nums.sort(reverse=True)
        # if len(set(nums)) == 1:
        #     return 0
        # else:
        #     while len(set(nums)) != 1:
        #         for i in range(len(nums)-1):
        #             if nums[i] != nums[i+1]:
        #                 nums[i] = nums[i+1]
        #                 count += 1
        #     return count