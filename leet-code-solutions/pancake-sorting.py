class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)):
            ind = arr.index(max(arr[:len(arr)-i]))
            ans.append(ind+1)
            ans.append(len(arr)-i)
            arr[:ind+1] = arr[:ind+1][::-1]
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
        return ans
      
            