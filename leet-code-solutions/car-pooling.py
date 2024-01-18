class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        val = []
        for  passenger,start,end in trips:
            val.append(start)
            val.append(end)
        n = max(val)
        ans = [0]*(n+1)
        for passenger,start,end in trips:
            ans[start] += passenger
            if end<n:
                ans[end] -= passenger
        prefix= [0]*(n+2)
        for i in range(len(ans)):
            prefix[i+1] = prefix[i] + ans[i]
        print(ans)
        print(prefix)
        if max(prefix) > capacity:
            return False
        return True
        