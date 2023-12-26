class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic = defaultdict(list)
        right_zero = nums.count(0)
        right_one = nums.count(1)
        left_one = 0
        left_zero = 0
        sums = 0
        for i in range(len(nums)+1):
            if i-1>=0:
                if nums[i-1] == 0:
                    right_zero -= 1
                    left_zero += 1
                else:
                    right_one -= 1
                    left_one += 1
            sums = right_one + left_zero
            dic[sums].append(i)
        return dic[max(dic.keys())]

        