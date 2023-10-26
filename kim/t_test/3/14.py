#11170

t = int(input())
a = []

for i in range(t):
    n, m = map(int, input().split())
    count = 0

    for j in range(n, m + 1):
        li = list(str(j))
        for k in li:
            if k == '0':
                count += 1
    a.append(count)

for i in a:
    print(i)