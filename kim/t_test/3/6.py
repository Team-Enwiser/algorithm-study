#10448

from itertools import combinations_with_replacement

a = []
for i in range(1, 45):
    a.append(int(i*(i+1)/2))

b = list(combinations_with_replacement(a, 3))

y = int(input())
for _ in range(y):
    x = int(input())
    for i in range(len(b)):
        if sum(b[i]) == x:
            print(1)
            break
        if i == (len(b) - 1):
            print(0)

from itertools import combinations_with_replacement

a = []
for i in range(1, 45):
    a.append(int(i*(i+1)/2))

b = list(combinations_with_replacement(a, 3))

c = []
y = int(input())
for _ in range(y):
    x = int(input())
    for i in range(len(b)):
        if sum(b[i]) == x:
            c.append(1)
            break
        if i == (len(b) - 1):
            c.append(0)           

for i in range(y):
    print(c[i])