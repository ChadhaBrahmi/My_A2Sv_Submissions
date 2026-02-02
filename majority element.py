class Solution(object):
    def majorityElement(self, nums):
        a = None
        count = 0
        
        for num in nums:
            if count == 0:
                a = num
            count += 1 if num == a else -1

        return a