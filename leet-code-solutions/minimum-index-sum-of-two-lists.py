class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mins = float("inf")
        dic = {}
        dic2 = defaultdict(list)
        ans = 0
        for index,value in enumerate(list2):
            dic[value] = index
        for index,value in enumerate(list1):
            if value in list2:
                ans = index + dic[value]
                dic2[ans].append(value)
                mins = min(mins,ans)
        return dic2[mins]

        
            

        