class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        unwanted = set()
        mins = float("inf")
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                unwanted.add(fronts[i])

        for i in range(len(fronts)):
            if fronts[i] not in unwanted:
                mins = min(mins,fronts[i])
            if backs[i] not in unwanted:
                mins = min(mins,backs[i])
        if mins == float("inf"):
            return 0
        else:
            return mins

        