class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        ans = (0,len(s)+1)
        target = Counter(t)
        count = Counter()
        def compare(x,y):
            for key in y:
                if x[key]<y[key]:
                    return False
            return True
        for right in range(len(s)):
            count[s[right]] += 1
            if compare(count,target):
                while left<len(s) and count[s[left]] > target[s[left]]:
                    count[s[left]] -= 1 
                    left += 1
                if right-left<ans[1]-ans[0]:
                    ans = (left,right)
        if ans[1]-ans[0]>len(s):
            return ""
        return s[ans[0]:ans[1]+1]

        