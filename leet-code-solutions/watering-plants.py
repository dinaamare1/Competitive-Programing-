class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_capacity = capacity
        for i in range(len(plants)):
            if plants[i] <= current_capacity:
                current_capacity -= plants[i]
                steps += 1
            else:
                steps += (i * 2)+1
                current_capacity = capacity
                current_capacity -= plants[i]
        return steps