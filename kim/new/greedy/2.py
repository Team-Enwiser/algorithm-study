a = list(map(int, input()))

result = 0

for i in a:
    if result ==0:
        result += i
        continue

    if i <= 1:
        result += i
    else:
        result *= i

print(result)

