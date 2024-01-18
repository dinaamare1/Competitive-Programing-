class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        result = 0
        counter_prefix = Counter()
        counter_prefix[0] = 1
        for num in nums:
            prefix += num
            result += counter_prefix[prefix-k] #adds the subarray with giving k sums when some previous element is are subtracted
            counter_prefix[prefix] += 1 # adds the prefix to the hashmap
        return result



        # uses prefix extra o(n) space 
#       -----------------------------------       
        # n = len(nums)
        # prefix = [0]*(n+1)
        # ans = 0
        # dic = defaultdict(int)
        # for i in range(len(nums)):
        #     prefix[i+1] = prefix[i] + nums[i]
        # for val in prefix:
        #     new = val+k
        #     ans += dic[val]
        #     dic[new] += 1
        # return ans