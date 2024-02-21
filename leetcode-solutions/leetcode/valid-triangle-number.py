class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        count = 0
        for x in range(len(nums)-1,-1,-1):
            r = x - 1 
            for l in range(x-1):
                while l < r and nums[l] + nums[r] > nums[x]:
                    r -= 1
                if l < r:
                    count += x-r-1
                else:
                    count += x-l-1
        return count
                        
                



            

                

        