class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)        
        if letters[0] <= target and letters[-1] <= target:
            return letters[0]
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right) // 2
            if letters[mid] <= target:
                left = mid +1
            elif letters[mid] > target:
                right = mid-1
        return letters[left]
        