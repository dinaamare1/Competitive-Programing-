class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        costs.sort(key=lambda x:abs(x[0]-x[1]),reverse=True)
        cityA = cityB = len(costs)//2
        for acost,bcost in costs:
            if (cityA and acost < bcost):
                total += acost
                cityA -= 1
            elif cityB == 0:
                total += acost
                cityA -= 1 
            else:
                total += bcost
                cityB -= 1
        return total
        