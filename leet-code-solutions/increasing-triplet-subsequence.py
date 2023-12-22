class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a,b = float("inf"),float("inf")
        for i in nums:
            if i>b:
                return True
            elif i<=a:
                a = i
            else:
                b = i
        return False
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] <= nums[j]:
        #             count += 1
        # if count >=3:
        #     return True
        # else:
        #     return False

        