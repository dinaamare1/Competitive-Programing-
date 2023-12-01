class Solution:
    def romanToInt(self, s: str) -> int:
        maps={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        val = 0
        for i in range(len(s)):
            if i+1 < len(s) and maps[s[i]] < maps[s[i+1]]:
                val -= maps[s[i]]
            else:
                val += maps[s[i]]
        return val
        # for i in range(0,len(s)):
        #     if i-1 >= 0 and s[i-1] == "C" and s[i] == "M":
        #         val -= 200
        #     if i-1 >= 0 and s[i-1] == "C" and s[i] == "D":
        #         val -= 200
        #     if i-1 >= 0 and s[i-1] == "X" and s[i] == "L":
        #         val -= 20
        #     if i-1 >= 0 and s[i-1] == "X" and s[i] == "C":
        #         val -= 20
        #     if i-1 >= 0 and s[i-1] == "I" and s[i] == "V":
        #         val -= 2
        #     if i-1 >= 0 and s[i-1] == "I" and s[i] == "X":
        #         val -= 2
        #     if s[i] in maps:
        #         val += maps[s[i]]
        # return val