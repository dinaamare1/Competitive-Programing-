class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        result = 0
        counter_prefix = Counter()
        counter_prefix[0] = 1
        for num in nums:
            prefix += num
            result += counter_prefix[prefix-goal]
            counter_prefix[prefix] += 1
        print(counter_prefix)
        return result
        


        # for num in nums:
        #     prefix += num
        #     result += counter_prefix[prefix-k] #adds the subarray with giving k sums when some previous element is are subtracted
        #     counter_prefix[prefix] += 1 # adds the prefix to the hashmap
        # return result