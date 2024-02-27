class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        while tickets[k] != 0:
            if tickets[i%len(tickets)] > 0:
                tickets[i%len(tickets)] -= 1
                count += 1
            i += 1
        return count

            

        