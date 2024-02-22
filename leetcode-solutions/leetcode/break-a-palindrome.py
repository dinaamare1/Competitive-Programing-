class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        strs = list(palindrome)
        if len(palindrome) == 1:
            return ""
        index = 0
        for idx,val in enumerate(strs):
            if val != "a":
                index = idx
                break
        
        strs[index] = "a"
        x = "".join(strs)
        if x != palindrome and x != x[::-1]:
            return x
        else:
            strs = list(palindrome)
            strs[-1] = "b"
            x = "".join(strs)
            if x != palindrome and x != x[::-1]:
                return x
            else:
                return ""


      

        