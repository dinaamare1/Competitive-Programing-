class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distanceP = abs(target[1])+abs(target[0])
        for ghost in ghosts:
            distanceGhost = abs(ghost[0]-target[0]) + abs(ghost[1]-target[1])
            if distanceGhost <= distanceP:
                return False
        return True
                

            

