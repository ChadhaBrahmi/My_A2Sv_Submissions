class Solution(object):
    def isPalindrome(self, x):
        
        l = str(x)
        reversed_l = l[::-1]
 
        return l == reversed_l
        