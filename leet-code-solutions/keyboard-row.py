class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        final=[]
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        for j in words:
            word=set(j.lower())
            if all(i in set1 for i in word) or all( i in set2 for i in word) or all        (i in set3 for i in word):
                final.append(j)
        return final  