class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sums = 0 
        new = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # new[0][0][0] = 1
        for i in range(len(grid)):
            maxs = max(grid[i])
            for j in range(len(grid[0])):
                new[i][j][0] = max(new[i][j][0],maxs)
        ans = []
        for i in range(len(grid)):
            maxs = 0
            for j in range(len(grid[0])):
                maxs = max(maxs,grid[j][i])
            ans.append(maxs)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                new[j][i][1] = max(new[j][i][1],ans[i])
        newGrid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                newGrid[i][j] = min(new[i][j][0],new[i][j][1])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sums += abs(newGrid[i][j]-grid[i][j])
        return sums


        