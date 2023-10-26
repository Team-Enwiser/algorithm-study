a = int(input())

result = 0

for i in range(0, a+1):
    if '3' in str(i):
        result += 3600
        continue
    for j in range(0, 60):
        if '3' in str(j):
            result += 60
            continue
        for k in range(0, 60):
            if '3' in str(k):
                result += 1

print(result)
