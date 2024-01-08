class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 0
        p2 =0
        # to check untill the end of the words <=
        while p1<=len(name) and p2<len(typed):
            if p1<len(name) and name[p1] == typed[p2]:
                p2 += 1
                p1 += 1
            elif p1>0 and typed[p2] == name[p1-1]:
                p2+= 1
            else:
                return False
        if p1 == len(name) and p2== len(typed):
            return True
        else:
            return False
