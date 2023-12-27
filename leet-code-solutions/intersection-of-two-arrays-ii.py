class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        ans = []
        for val in nums2:
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1 
        for val in nums1:
            if val in dic:
                if dic[val] == 0:
                    del dic[val]
                else:
                    ans.append(val)
                    dic[val] -= 1
        return ans