class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            sums = 0
            for j in range(len(boxes)):
                if boxes[j] != "0":
                    sums += abs(i-j)
            ans.append(sums)
        return ans