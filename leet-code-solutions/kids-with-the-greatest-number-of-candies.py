class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = [True]*(len(candies))
        for index in range(len(candies)):
            candies[index] += extraCandies
            if candies[index] >= max_candy:
                result[index] = True
            else:
                result[index] = False
        return result
