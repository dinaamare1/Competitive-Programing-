class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_log = defaultdict(int)
        self.time_to_live = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.time_log[tokenId] = currentTime +self.time_to_live
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.time_log[tokenId] > currentTime:
            self.time_log[tokenId] = currentTime + self.time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for val in self.time_log.values():
            if val > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)