n = 5#int(input())
counter = 0
for i in range(n + 1):
    if i % 10 == 3:
        counter += 60*60
        continue
    for m in range(60):
        if m % 10 == 3:
            counter += 60
            continue
        if m // 10 == 3:
            counter += 60
            continue        
        for n in range(60):
            if n % 10 == 3:
                counter += 1
                continue
            if n // 10 == 3:
                counter += 1
                continue

print(counter)
