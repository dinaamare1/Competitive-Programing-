class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=blocks[:k].count("W")
        mins= count
        for i in range(1,len(blocks)-k+1):
            if blocks[i+k-1]=="W":
                count+=1
            if blocks[i-1]=="W":
                count-=1
            mins=min(count,mins)
        return mins
        
            
