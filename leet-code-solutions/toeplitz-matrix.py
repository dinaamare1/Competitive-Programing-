class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # for row in range(len(matrix) - 1):
        #     if matrix[row][0:-1] != matrix[row+1][1:]:
        #         return False
        # return True
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
        
        