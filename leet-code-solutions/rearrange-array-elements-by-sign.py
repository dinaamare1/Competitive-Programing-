class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        p1 = 0
        p2 = 0
        while p1<len(pos):
            ans.append(pos[p1])
            ans.append(neg[p2])
            p1 += 1
            p2 += 1
        return ans


