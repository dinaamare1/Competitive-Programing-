class Solution:
    def freqAlphabets(self, s: str) -> str:
        val = ""
        s = s[::-1]
        i = 0
        while i < len(s):
            if s[i] == "#":
                value = s[i+2] + s[i+1]
                val += chr(int(value) + 96)
                i += 3
            else:
                val += chr(int(s[i])+96)   
                i+=1
        return val[::-1]