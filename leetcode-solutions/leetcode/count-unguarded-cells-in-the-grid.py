class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for i in range(m)]
        for g in guards:
            grid[g[0]][g[1]] = "G"
        for w in walls:
            grid[w[0]][w[1]]  = "W"
      
        for i in range(m):
            guarded = False
            for j in range(n):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
            guarded = False
            for j in range(n-1,-1,-1):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
            
        for j in range(n):
            guarded = False
            for i in range(m):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
            guarded = False
            for i in range(m-1,-1,-1):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
        
        count  = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count+=1
        return count








        # count = 0
        # uncount = 0
        # countW = len(walls)
        # countG = len(guards)
        # sets = set()
        # grid = [[0]*n for _ in range(m)]
        # for i,j in guards:
        #     grid[i][j] = "G"
        # for i,j in walls:
        #     grid[i][j] = "W"
        # print(grid)
        # for row in range(m):
        #     for col in range(n):
        #         print("new")
        #         if grid[row][col] == "G":
        #             for y in range(len(grid[0])):
        #                 if grid[row][y] == "W":
        #                     break
        #                 elif grid[row][y] == "G":
        #                     continue
        #                 else:
        #                     if (row,y) not in sets:
        #                         count += 1
        #                         sets.add((row,y))
        #                 print("y",row,y,count,grid[row][y])
        #             for y in range(row+1,len(grid[0])):
        #                 if grid[row][y] == "W":
        #                     break
        #                 elif grid[row][y] == "G":
        #                     continue
        #                 else:
        #                     if (row,y) not in sets:
        #                         count += 1
        #                         sets.add((row,y))
        #                 print("y",row,y,count,grid[row][y])
        #             for x in range(len(grid)): 
        #                 if grid[x][col] == "W":
        #                     break
        #                 elif grid[x][col] == "G":
        #                     continue
        #                 else:
        #                     if (x,col) not in sets:
        #                         count += 1
        #                         sets.add((x,col))
        #                 print("x",x,col,count)
        #             for x in range(col+1,len(grid)): 
        #                 if grid[x][col] == "W":
        #                     break
        #                 elif grid[x][col] == "G":
        #                     continue
        #                 else:
        #                     if (x,col) not in sets:
        #                         count += 1
        #                         sets.add((x,col))
        #                 print("x",x,col,count)
            
        # print(sets)
        # return m*n - (countG+countW+count)