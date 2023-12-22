class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = [str(num) for num in digits]
        nums = "".join(nums)
        nums = [num for num in str(int(nums)+1)]
        nums =[int(num) for num in nums]
        return nums