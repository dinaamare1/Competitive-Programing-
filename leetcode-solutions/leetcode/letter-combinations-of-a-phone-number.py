class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        bucket = []
        def backtrack(idx):
            if len(digits) == len(bucket) and len(digits)>0:
                ans.append("".join(bucket[:]))
                return
            for i in range(idx,len(digits)):
                for j in range(len(phone[digits[idx]])):
                    bucket.append(phone[digits[idx]][j])
                    backtrack(i+1)
                    bucket.pop()
        backtrack(0)
        return ans
        