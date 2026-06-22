class Solution:
    def twoSum(self, nums, target):
        values = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in values:
                return [values[needed], i]
            values[nums[i]] = i
