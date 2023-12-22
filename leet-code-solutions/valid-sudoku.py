class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_count = defaultdict(set)
        row_count =  defaultdict(set)
        sqrs = defaultdict(set)
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                box = (row//3)*10 + (col//3) 
                if val != ".":
                    if val in col_count[col] or val in row_count[row] or val in sqrs[box]:
                        return False
                    col_count[col].add(val)
                    row_count[row].add(val)
                    sqrs[box].add(val)
        return True
