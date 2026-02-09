class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        v = [0] * n

        for i in range(n):
            for j in range(n):
                if nums[i] < nums[j]:
                    v[j] += 1

        return v
