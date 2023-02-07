inputList = list(input())
result = 0

for i in inputList:
    i = int(i)
    if result * i >= result + i:
        result *= i
    else:
        result += i

print(result)