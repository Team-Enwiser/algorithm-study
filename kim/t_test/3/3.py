#2309

from itertools import combinations

a = []
for _ in range(9):
    a.append(int(input()))

b = [0, 1, 2, 3, 4, 5, 6, 7, 8]
c = list(combinations(b, 7))
d = []

for i in range(len(c)):
    result = 0
    for j in range(7):
        result += a[c[i][j]]

    if result == 100:
        for k in range(7):
            d.append(a[c[i][k]])
        break

d.sort()
for i in range(7):
    print(d[i])
