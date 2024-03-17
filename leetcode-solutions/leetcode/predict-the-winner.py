class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        played = {}

        def choice(left, right):
            if left == right:
                return nums[left]
            
            if (left, right) in played:
                return played[(left, right)]

            pickLeft = nums[left] - choice(left + 1, right)
            pickRight = nums[right] - choice(left, right - 1)
            played[(left, right)] = max(pickLeft, pickRight)
            return played[(left, right)]

        return choice(0, len(nums) - 1) >= 0
