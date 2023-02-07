a, b = map(int, input().split())

counter = 0

while 1:
    if a % b == 0:
        a = int(a / b)
    else :
        a = a - 1

    counter += 1

    if a == 1:
        break

print(counter)