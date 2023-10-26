#1182
from itertools import combinations

n, s = map(int, input().split())

a = list(map(int, input().split()))

b = []

for i in range(1, n + 1):
    li = list(combinations(a, i))
    b.append(li)

count = 0

for i in b:
    for j in range(len(i)):
        if sum(i[j]) == s: count += 1

print(count)
