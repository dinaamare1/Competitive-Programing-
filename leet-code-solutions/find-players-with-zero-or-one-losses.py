class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = []
        loser = []
        winans = set()
        loseans = []
        result = []
        for win,lose in matches:
            winner.append(win)
            loser.append(lose)
        losers = set(loser.copy())
        for i in winner:
            if i not in losers:
                winans.add(i)
        losercount = Counter(loser)
        for i in losercount:
            if losercount[i] == 1:
                loseans.append(i)
        winans = list(winans)
        winans.sort()
        loseans.sort()
        return [winans,loseans]



        