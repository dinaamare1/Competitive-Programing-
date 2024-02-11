class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        index = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count<=2:
                nums[index] = nums[i]
                index += 1
        return index


        # count = 0
        # h = 0
        # s = 1
        # while s<len(nums):
        #     if nums[h] == nums[s]:
        #         count += 1
        #         if nums[h] == nums[s] and count > 1:
        #             nums[s] = "_"
        #         s += 1
        #     if s<len(nums) and nums[h] != nums[s]:
        #         count = 0
        #         h = s
        #         s = h + 1
        # h1 = 0
        # s1 = 0
        # while s1< len(nums):
        #     if nums[s1] != "_":
        #         nums[h1],nums[s1] = nums[s1],nums[h1]
        #         h1 += 1
        #     s1 += 1
        # return h1
            
        