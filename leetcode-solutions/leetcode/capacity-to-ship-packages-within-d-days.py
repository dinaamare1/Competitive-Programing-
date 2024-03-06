class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkDays(mid):
            sums = 0
            count = 1
            for weight in weights:
                sums += weight
                if sums> mid:
                    count += 1
                    sums = weight
                
            return count

        upper = sum(weights) + 1
        lower = max(weights) - 1
        while lower + 1 < upper:
            mid = ((lower + upper) // 2)
            print(mid,lower,upper)
            vals = checkDays(mid)
            print(vals)
            if vals <= days:
                upper = mid
            else:
                lower = mid
        return upper


            
