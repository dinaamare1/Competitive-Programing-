class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s =  [ord(letter) for letter in s]
        ans =  [0]*(len(s)+1)
        for start,end,direction in shifts:
            if direction == 0:
                ans[start] += -1
                ans[end+1] += 1
            else:
                ans[start] += 1
                ans[end+1] += -1
        ref = [0]*(len(ans))
        for i in range(len(ans[:-1])):
            ref[i+1] = ref[i] + ans[i]
        return "".join([chr(((a+b) - 97) % 26 + 97) for a,b in zip(s,ref[1:]) ])
