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
        upper = sum(weights)
        lower = max(weights)
        while lower <= upper:
            mid = ((lower + upper) // 2)
            vals = checkDays(mid)
            
            if vals <= days:
                upper = mid -1
            else:
                lower = mid + 1
        return lower


            
