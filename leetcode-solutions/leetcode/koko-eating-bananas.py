class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def hours(h):
            hour = 0
            for pile in piles:
                hour += ceil(pile/h)

            return hour
        print(hours(6))
        # return 0
        lower = 1
        upper = max(piles)
        if hours(lower) == h:
            return lower
        elif hours(upper) == h:
            return upper
        while lower <= upper:
            mid = (lower+upper)//2
            check = hours(mid)
            if check <= h:
                upper = mid -1
            else:
                lower = mid+1
        return upper + 1
            

            