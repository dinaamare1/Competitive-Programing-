class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        cols = len(board[0])
        sets = set()
        def backtrack(r,c,idx):
            if idx == len(word):
                return True
            if r<0 or c<0 or r>=row or c>=cols or (r,c) in sets or word[idx] != board[r][c]:
                return False
            sets.add((r,c))
           
            ans = (backtrack(r+1,c,idx+1) or backtrack(r-1,c,idx+1) or backtrack(r,c+1,idx+1) or backtrack(r,c-1,idx+1))
            sets.remove((r,c))
            return ans
        for i in range(row):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True
        return False




        