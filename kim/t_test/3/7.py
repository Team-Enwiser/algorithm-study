#13410

n, k = map(int, input().split())
li = []

for j in range(1, (k+1)):
    a = str(n*j)
    li.append(int(a[::-1]))

print(li[k-1])