#2851

a = []
for _ in range(10):
    a.append(int(input()))

b = []
b.append(100)
for i in range(1, 11):
    b.append(100 - sum(a[0:i]))

b = sorted(b, key=abs)

if abs(b[0]) == abs(b[1]):
    print(100 - b[1])
else:
    print(100 - b[0])
