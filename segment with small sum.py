a, b = map(int, input().split())
c = list(map(int, input().split()))

d = 0
e = 0
f = 0

for g in range(a):
    e += c[g]
    while e > b:
        e -= c[d]
        d += 1
    f = max(f, g - d + 1)

print(f)
