class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r =len(matrix)-1
        while l<=r:
            mid = (l+r) // 2
            if matrix[mid][0] <= target:
                l= mid + 1
            else:
                r = mid - 1
        left = 0
        right = len(matrix[r])-1
        while left<=right:
            mid = (left+right) // 2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                left= mid + 1
            else:
                right = mid - 1
        return False
        