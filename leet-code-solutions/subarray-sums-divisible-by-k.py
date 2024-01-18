class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        result = 0
        counter_prefix = Counter()
        counter_prefix[0] = 1
        for num in nums:
            prefix += num
            result += counter_prefix[prefix%k]
            counter_prefix[prefix%k] += 1
        return result



        # n = len(nums)
        # prefix = [0]*(n+1)
        # for i in range(n):
        #     prefix[i+1] = prefix[i] + nums[i]
        # ans = 0
        # dic= defaultdict(int)
        # for val in prefix:
        #     x = val%k
        #     ans += dic[x]
        #     dic[x] += 1
        # return ans
        