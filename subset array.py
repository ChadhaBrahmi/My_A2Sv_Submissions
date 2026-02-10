class Solution:
    def isSubset(self, a, b):
        c = {}
        for i in a:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        for i in b:
            if i not in c or c[i] == 0:
                return False
            c[i] -= 1
        return True
