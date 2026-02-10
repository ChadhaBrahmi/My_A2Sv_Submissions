class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        a.sort()
        b.sort()
        for x, y in zip(a, b):
            if x != y:
                return False
        return True
