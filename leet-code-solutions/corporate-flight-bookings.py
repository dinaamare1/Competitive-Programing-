class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for first,second,seat in bookings:
            ans[first] += seat
            if second+1<=n:
                ans[second+1] -= seat
        prefix = [0]*(len(ans))
        for i in range(len(ans)):
            prefix[i]= prefix[i-1] + ans[i]
        return prefix[1:]
