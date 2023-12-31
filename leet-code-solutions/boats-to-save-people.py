class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        boat = 0
        while l<=r:
            if people[l] + people[r] <= limit:
                l+=1
            boat += 1
            r -= 1
        return boat
        # people.sort()
        # l = 0
        # r = len(people)-1
        # boat = 0
        # while l<=r:
        #     if people[l] + people[r] <= limit:
        #         boat += 1
        #         l+=1
        #         r-=1
        #     else:
        #         boat += 1
        #         r -= 1
        # return boat