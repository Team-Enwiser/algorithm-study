a = list(input())
a.sort()

count = 0

for i in a:
    if ord(i) >= 97:
        break
    count += 1

print(''.join(a[count:len(a)]+a[0:count]))