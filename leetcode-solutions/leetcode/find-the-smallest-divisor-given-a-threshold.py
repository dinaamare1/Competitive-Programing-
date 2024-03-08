class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(val):
            sums = 0
            for num in nums:
                sums += ceil(num/val)
            return sums
        print(check(44))
        left = 0
        right = max(nums)+1
        while left + 1< right:
            mid = (left + right) // 2
            value =  check(mid)
            if value <= threshold:
                right = mid
            else:
                left = mid
        return right

