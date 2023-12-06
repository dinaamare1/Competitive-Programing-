class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        n =  len(nums)//2
        for index in range(len(nums)):
            if index + n <len(nums):
                result.append(nums[index])
                result.append(nums[index+n])
        return result

        