class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = defaultdict(list)
        for idx,val in enumerate(nums):
            dic[val].append(idx)
        res = [0] * len(nums)
        for idxs in dic.values():
            if len(idxs) == 1:
                continue
            left_count = 0
            left_sums= 0
            right_count = len(idxs)
            right_sums= sum(idxs)
            for index in idxs:
                right_count -= 1
                right_sums -= index
                res[index] = (
                    (left_count * index - left_sums)
                    + (right_sums - right_count * index)
                )
                left_count += 1
                left_sums += index
        return res