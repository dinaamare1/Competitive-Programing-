class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        r = len(s) -1 
        nums = list(s)
        count = 0
        while l<r:
            if nums[l] == "1" and nums[r] == "0":
                nums[l],nums[r] = nums[r],nums[l]
                count += r - l
                l += 1
                r -= 1
            elif nums[r] == "1" and nums[l] == "1":
                r -= 1
            else:
                l += 1
        print(nums)
        return count