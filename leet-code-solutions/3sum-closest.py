class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mins = float("inf")
        closest = 0

        for idx, num in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            while l < r:
                sums = num + nums[l] + nums[r]
                diff = abs(sums - target)
                if diff < mins:
                    mins = diff
                    closest = sums
                if sums == target:
                    return closest
                elif sums < target:
                    l += 1
                else:
                    r -= 1
        return closest
