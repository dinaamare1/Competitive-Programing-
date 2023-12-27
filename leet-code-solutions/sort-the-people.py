class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # bubble sort
        # we keep swapping untill the array is sorted, holding two adjecent points

        # while heights != sorted(heights):
        #     for i in range(len(heights)):
        #         if i+1<len(heights) and heights[i] > heights[i+1]:
        #             heights[i],heights[i+1] = heights[i+1],heights[i]
        #             names[i],names[i+1] = names[i+1],names[i]
        # return names[::-1]




        # selection sort
        # we select the min and swap on each iterations

        while heights != sorted(heights):
            for i in range(len(heights)):
                for j in range(i+1,len(heights)):
                    if heights[i]>heights[j]:
                        heights[i],heights[j] = heights[j],heights[i]
                        names[i],names[j] = names[j],names[i]
        return names[::-1]
        