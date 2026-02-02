class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = n * (n + 1) // 2
        total = sum(nums)
        return 0 if total == a else abs(a - total)
        