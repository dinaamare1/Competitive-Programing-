class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap=dict()
        for i in range(len(order)):
            hashmap[order[i]]=i
        for i in range(len(words)-1):
            if max(words[i],words[i+1], key=lambda x:[hashmap[chr] for chr in x])!=(words[i+1]):
                return False
        return True