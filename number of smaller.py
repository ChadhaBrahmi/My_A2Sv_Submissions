a, b = map(int, input().split())
c = list(map(int, input().split()))
d = list(map(int, input().split()))

def count_less(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

for x in d:
    print(count_less(c, x), end=' ')
