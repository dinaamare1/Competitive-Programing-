class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        self.fairness = float("inf")
        def choices(i,bucket):
            if i >= len(cookies):
                self.fairness = min(self.fairness,max(bucket))
                return
            if max(bucket) > self.fairness:
                return
            for j in range(k):
                bucket[j] += cookies[i]
                choices(i+1,bucket)
                bucket[j] -= cookies[i]
        choices(0,bucket)
        return self.fairness

        