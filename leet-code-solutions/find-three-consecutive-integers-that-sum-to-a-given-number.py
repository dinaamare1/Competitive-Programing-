class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # i = 1
        # while i < num:
        #     if num == (i-1)+(i)+(i+1):
        #         return [i-1,i,i+1]
        #     i+=1
        # return []
        if num % 3 == 0:
            i = num // 3
            return [i-1,i,i+1]
        return []