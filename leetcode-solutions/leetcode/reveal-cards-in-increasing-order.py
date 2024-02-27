class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        indexs = deque([val for val in range(n)])
        ans = [0] * n
        for idx, num in enumerate(sorted(deck)):
            ans[indexs.popleft()] = num
            if indexs:
                indexs.append(indexs.popleft())
        return ans
        