class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxs = 0
        for i in range(n-2):
            for j in range(m-2):
                sums = 0
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        sums += grid[row][col]
                print(sums)
                sums = sums-(grid[i+1][j]+grid[i+1][j+2])
                print(sums)
                maxs = max(maxs,sums)
        return maxs