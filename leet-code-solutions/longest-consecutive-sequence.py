class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sets= set(nums)
        maxs= 0
        for num in sets:
            if num - 1 not in sets:
                curr = num
                currLength = 1
                while curr + 1 in sets:
                    curr += 1
                    currLength += 1
                maxs = max(maxs, currLength)
        return maxs

    # using sort
        # Sortednums = sorted(set(nums))
        # maxs = 1
        # count = 0 
        # if not Sortednums:
        #     return 0
        # for i in range(len(Sortednums)-1):
        #     if abs(Sortednums[i+1] - Sortednums[i]) == 1:
        #         count += 1
        #         maxs = max(maxs,count+1)
        #     else:
        #         count = 0
        # return maxs