class Solution:
    def splitString(self, s: str) -> bool:
        bucket = []
        def backtrack(idx):
            if idx>=len(s):
                for i in range(1,len(bucket)):
                    if bucket[i-1] - bucket[i] != 1:
                        return False
                return len(bucket)>=2
            for i in range(idx,len(s)):
                val = int(s[idx:i+1])
                if len(bucket) == 0 or val ==  bucket[-1] - 1:
                    bucket.append(val)
                    if backtrack(i+1):
                        return True
                    bucket.pop()
            return False
        return backtrack(0)

        