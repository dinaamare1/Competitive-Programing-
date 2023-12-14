class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        ans = []
        for cpdomain in cpdomains:
            times,strs = cpdomain.split()
            dic[strs] += int(times)
            for i in range(len(strs)):
                if strs[i] == ".":
                    dic[strs[i+1:]] += int(times)
        for key,value in dic.items():
            res = [str(value),key]
            ans.append(" ".join(res))
        return ans

