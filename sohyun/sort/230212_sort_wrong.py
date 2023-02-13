n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    a[i] = b[i]
result = 0
for e in a:
    result += e
print(result)
