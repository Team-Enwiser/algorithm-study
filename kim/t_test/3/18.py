n = int(input())

a = []

for i in range(666, 2699999):
    if '666' in str(i):
        a.append(i)


print(a[n-1])