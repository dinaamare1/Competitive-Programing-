class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        mins = float("inf")
        dic = defaultdict(int)
        if len(set(cards)) == len(cards):
            return -1
        for right in range(len(cards)):
            dic[cards[right]] += 1
            while dic[cards[right]]>1:
                mins = min(mins,right - left+1)
                dic[cards[left]] -= 1
                left += 1
            
        return mins
