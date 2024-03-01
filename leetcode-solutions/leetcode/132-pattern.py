class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mins = float("-inf")
        count = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < mins:
                return True
            while stack and stack[-1]<nums[i]:
                mins = stack.pop()
            stack.append(nums[i])
        return False
        