class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
         s = ""
         t = ""

         for i in range(len(word1)):
             s += word1[i]
    
         for j in range(len(word2)):
             t += word2[j]

         return s == t
        