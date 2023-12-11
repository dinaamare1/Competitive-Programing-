class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        return max(arr, key=count.get)
        # dic = defaultdict(int)
        # maxs = 0
        # for i in arr:
        #     dic[i] += 1
        # for i in dic:
        #     maxs = max(maxs,dic[i])
        # for i in dic:
        #     if dic[i] == maxs:
        #         return i
        