class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maps = {}
        for idx,val in enumerate(arr2):
            maps[val] = idx
        def solver(val):
            if val in maps:
                return maps[val]
            else:
                return val+1000
        arr1.sort(key=solver)
        return arr1