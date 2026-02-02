class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            a = target - nums[i]
            if a in nums[i+1:]:
                return [i, nums[i+1:].index(a) + (i+1)]
            i += 1
        return []
        