class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for index, item in reversed(list(enumerate(nums[:-1]))):
            if index + item >= goal:
                goal = index
        print(goal)
        return goal == 0