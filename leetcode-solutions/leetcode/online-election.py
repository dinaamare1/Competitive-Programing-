class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.person = []
        maxs = float("-inf")
        leads = float("-inf")
        dic = defaultdict(int)
        for person, time in zip(persons, times):
            dic[person] += 1
            if dic[person] >= maxs:
                maxs = dic[person]
                leads = person
            self.person.append([time,leads])
    def q(self, t: int) -> int:
        left = -1
        right = len(self.person)
        while left + 1< right:
            mid = (left+right)//2
            if self.person[mid][0] > t:
                right = mid
            else:
                left = mid
        return self.person[left][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)