#18512

x, y, p1, p2 = map(int, input().split())
limit = 100

i = 0
j = 0

while True:
    a = p1 + i * x
    b = p2 + j * y
    if a == b:
        print(a)
        break
    elif a > b:
        j += 1
    else:
        i += 1

    if i == limit or j == limit:
        print(-1)
        break
    