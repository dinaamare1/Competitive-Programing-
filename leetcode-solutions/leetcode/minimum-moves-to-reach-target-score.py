class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        i = target
        while i>1:
            if maxDoubles > 0 and i%2==0:
                i -= i//2
                maxDoubles -= 1
                count += 1 
            elif maxDoubles == 0:
                count += i - 1
                i = 1
            else:
                i-=1
                count += 1
        return count

        