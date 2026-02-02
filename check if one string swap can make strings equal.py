class Solution(object):
    def areAlmostEqual(self, s1, s2):
         if s1 == s2:
             return True

         dif = [i for i in range(len(s1)) if s1[i] != s2[i]]
   
         if len(dif) != 2:
              return False
         return s1[dif[0]] == s2[dif[1]] and s1[dif[1]] == s2[dif[0]]
        