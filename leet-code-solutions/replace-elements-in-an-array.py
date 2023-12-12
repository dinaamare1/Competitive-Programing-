class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        ans = [0]*(len(nums))
        for index,value in enumerate(nums):
            dic[value] = index
        for op1,op2 in operations:
            dic[op2] = dic.pop(op1)
            # print(dic[op2],dic[op1])
        for key,value in dic.items():
            ans[value] = key
        return ans


