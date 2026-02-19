class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        a = {}
        b = {}
        c = 0
        res = []

        for x, y in queries:
            if x in a:
                old = a[x]
                b[old] -= 1
                if b[old] == 0:
                    del b[old]
                    c -= 1

            a[x] = y

            if y in b:
                b[y] += 1
            else:
                b[y] = 1
                c += 1

            res.append(c)

        return res
