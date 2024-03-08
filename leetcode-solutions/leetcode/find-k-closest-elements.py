class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        def search(left,right):
            while left+1<right:
                mid = (left+right)//2
                if arr[mid] <= x:
                    left = mid
                else:
                    right = mid
            return left
        midPoint = search(-1,len(arr))
        left,right = midPoint,midPoint + 1
        while len(ans)<k and left >=0 and right<len(arr):
            if abs(arr[left]-x) <= abs(arr[right]-x):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        while len(ans)<k and left >=0:
            ans.append(arr[left])
            left -= 1
        while len(ans) < k and right<len(arr):
            ans.append(arr[right])
            right += 1
        return sorted(ans)







