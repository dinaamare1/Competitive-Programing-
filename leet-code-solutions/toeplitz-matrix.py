class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix) - 1):
            if matrix[row][0:-1] != matrix[row+1][1:]:
                return False
        return True
        
        