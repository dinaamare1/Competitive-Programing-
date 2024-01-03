class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = defaultdict(list)
        ans = []
        for x,y in points:
            dic[sqrt(x**2+y**2)].append([x,y])
        for val in sorted(dic):
            ans.extend(dic[val])
        return ans[:k]

