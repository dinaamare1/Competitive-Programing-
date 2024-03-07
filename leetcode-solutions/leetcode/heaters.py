class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int: 
        maxs = float("-inf")
        heaters.sort()
        for i in range(len(houses)):
            mins = float("inf")
            left = 0
            right = len(heaters) -1
            while left<=right:
                print(mins)
                mid = (right + left)//2
                if houses[i] <=heaters[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                mins = min(mins,abs(houses[i]-heaters[mid]))
            maxs = max(maxs,mins)
        return maxs


                


        # def check(mids):
        #     length = 1
        #     for heat in heaters:
        #         length += heat + mids
        #         print("idx",heat,idx,new)
        #     if len(heaters)>1:
        #         return length - len(heaters)
        #     return length
        # print(check(1),check(2),check(3),check(4))
        # # return 1
        # left = 0
        # right = max(max(heaters),max(houses)) + 1
        # while left+1<right:
        #     mid = (left+right) // 2
        #     val = check(mid)
        #     print(mid,val,left,right)
        #     if val <= max(max(houses),max(heaters)):
        #         left = mid
        #     else:
        #         right = mid
        # print(left,right)
        # return left
