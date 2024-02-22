class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxStack = deque()
        minStack = deque()
        maxs = float("-inf")
        l = 0
        for r in range(len(nums)):
            while maxStack and maxStack[-1] < nums[r]:
                maxStack.pop()
            maxStack.append(nums[r])
            while minStack and minStack[-1] > nums[r]:
                minStack.pop()
            minStack.append(nums[r]) 
            while minStack and maxStack and abs(minStack[0]-maxStack[0]) > limit:
                if nums[l] == maxStack[0]:
                    maxStack.popleft()
                elif nums[l] == minStack[0]:
                    minStack.popleft()
                l += 1 
            maxs = max(maxs,r-l+1)
        return maxs


