class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse =True)
        maxs = float("-inf")
        print(tasks)
        for i in range(len(processorTime)):
            for j in range(4):
                maxs = max(maxs,(tasks[(4*i)+j])+processorTime[i])
        return maxs