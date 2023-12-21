class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and (i * j) % k == 0 :
        #             count += 1
        # return count
        dic = {}
        count = 0
        for index,val in enumerate(nums):
            if val not in dic:
                dic[val] = [index]
            else:
                for prev_index in dic[val]:
                    if (prev_index * index) % k == 0:
                        count += 1
                dic[val].append(index)
        print(dic)
        return count
