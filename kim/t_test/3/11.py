from itertools import combinations

a = list(map(int, input().split()))

a.sort()
b = list(combinations(a, 3))
flag = False

for i in range(a[2], a[0]*a[1]*a[2]+1):
    for j in b:
        if i % j[0] == 0 and i % j[1] == 0 and i % j[2] == 0:
            print(i)
            flag = True
            break
    if flag: break

from itertools import combinations

a = list(map(int, input().split()))

a.sort()
b = list(combinations(a, 3))

for i in range(a[2], a[0]*a[1]*a[2] + 1):
    for j in b:
        if i % j[0] == 0 and i % j[1] == 0 and i % j[2] == 0:
            print(i)
            exit(0)
    