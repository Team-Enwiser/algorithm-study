#10951

n = int(input())
a = 0
b = 0
c = 0
if n == 2:
    a, b = map(int, input().split())
else:
    a, b, c = map(int, input().split())

li = []

for i in range(max(a, b, c)):
    x = i + 1
    if a % x == 0 and b % x == 0 and c % x == 0:
        li.append(x)

for j in range(len(li)):
    print(li[j])