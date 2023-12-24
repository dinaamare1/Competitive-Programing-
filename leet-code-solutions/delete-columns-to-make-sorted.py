class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = [list(strss) for strss in strs]
        count = 0
        transposed = [[0]*len(strs) for _ in range(len(strs[0]))]
        for row in range(len(strs)):
            for col in range(len(strs[0])):
                transposed[col][row] = strs[row][col]
        for trans in transposed:
            if trans != sorted(trans):
                count += 1
        return count