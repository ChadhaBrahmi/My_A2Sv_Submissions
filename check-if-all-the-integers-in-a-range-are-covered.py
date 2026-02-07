class Solution(object):
    def isCovered(self, ranges, left, right):
        for x in range(left, right + 1):
            ok = False
            for a, b in ranges:
                if a <= x <= b:
                    ok = True
                    break
            if not ok:
                return False
        return True
