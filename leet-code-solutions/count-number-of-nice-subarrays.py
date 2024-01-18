class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            count = 0
            l = 0
            for r in range(len(nums)):
                if nums[r] %2:
                    k -= 1
                while k <0:
                    if nums[l] %2:
                        k += 1
                    l += 1
                count += r - l + 1
            return count
        return atmost(k) -atmost(k-1)


