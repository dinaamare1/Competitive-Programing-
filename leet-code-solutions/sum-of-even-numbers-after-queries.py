class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum(x for x in nums if x % 2 == 0)
        result = []
        for val, index in queries:
            oldValue, nums[index] = nums[index], nums[index] + val

            if oldValue % 2 == 0:
                even -= oldValue

            if nums[index] % 2 == 0:
                even += nums[index]

            result.append(even)

        return result




        # the code is too long

        # even = sum(x for x in nums if x % 2 == 0)
        # result = []

        # for val,index in queries:
        #     if nums[index] % 2:
        #         if (nums[index] + val) % 2 == 0:
        #             even += nums[index]+val
        #             nums[index] += val
        #             result.append(even)
        #         else:
        #             nums[index] += val
        #             result.append(even)
        #     else:
        #         if (nums[index] + val) % 2 == 0:
        #             nums[index] += val
        #             even += val
        #             result.append(even)
        #         else:
        #             even -= nums[index]
        #             nums[index] += val
        #             result.append(even)
        # return result 

        

        # Time limit excedded
        # sums = 0
        # result = []
        # for val,index in queries:
        #     nums[index] += val
        #     sums = sum(map(lambda x: x if x % 2 == 0 else 0, nums))
        #     result.append(sums)
        # return result
        