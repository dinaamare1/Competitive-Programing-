class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = deque(senate)
        banned_R = 0
        banned_D = 0

        while len(set(senate)) > 1:
            senator = senate.popleft()
            if senator == "R":
                if banned_R > 0:
                    banned_R -= 1
                else:
                    banned_D += 1
                    senate.append(senator)
            else:
                if banned_D > 0:
                    banned_D -= 1
                else:
                    banned_R += 1
                    senate.append(senator)
        if senate[0] == "R":
            return "Radiant"
        return "Dire"
