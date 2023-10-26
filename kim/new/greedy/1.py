a, b = map(int, input().split())

count = 0

while True:
    if a % b == 0:
        a = a//b
    else:
        a -= 1

    count += 1

    if a == 1:
        break

print(count)
