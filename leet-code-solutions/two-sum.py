class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index,val in enumerate(nums):
            dic[val] = index
        for index,val in enumerate(nums):
            diff = target - val
            if diff in dic and dic[diff] != index:
                return [dic[diff],index]  
                            