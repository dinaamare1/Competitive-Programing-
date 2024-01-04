class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        sums = 0
        while l<r:
            target = skill[0] + skill[-1]
            if skill[l] + skill[r] == target:
                sums += (skill[l] * skill[r])
                l+=1
                r-=1
            else:
                return -1
        return sums