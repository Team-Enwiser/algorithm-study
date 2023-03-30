#2798
from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))

b = list(combinations(a, 3))
c = []

for i in range(len(b)):
    x = m - sum(b[i])
    c.append(x)

c.sort()

for i in range(len(b)):
    if c[i] >= 0:
        print(m - c[i])
        break