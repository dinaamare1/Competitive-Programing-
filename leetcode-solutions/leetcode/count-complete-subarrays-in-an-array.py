class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        left = 0
        maps = defaultdict(int)
        for right in range(len(nums)):
            maps[nums[right]] += 1
            while len(set(nums)) == len(maps):
                # print(left,right,count,maps)
                if maps[nums[left]] == 1:
                    maps.pop(nums[left])
                else:
                    maps[nums[left]] -=1
                left += 1
            count += left
        return count
            