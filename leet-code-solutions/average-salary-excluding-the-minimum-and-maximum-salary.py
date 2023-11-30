class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        avarageSum = sum(salary)-(salary[0]+salary[-1])
        avarage = avarageSum / (len(salary) - 2)
        return avarage