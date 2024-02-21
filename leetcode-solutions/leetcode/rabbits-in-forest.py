class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = defaultdict(int)
        for idx,val in enumerate(answers):
            if val in dic:
                dic[val] -= 1
            else:
                dic[val] = val
            if dic[val] == 0:
                del dic[val]
        count = len(answers)
        for key,val in dic.items():
            count += val 
        return count