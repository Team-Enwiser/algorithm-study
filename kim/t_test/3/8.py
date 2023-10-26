#18312

n, k = map(int, input().split())

count = 0

for a in range(n+1):
    if a // 10 == k:
        count += 3600
        continue
    if a % 10 == k:
        count += 3600
        continue
    for b in range(60):
        if b // 10 == k:
            count += 60
            continue
        if b % 10 == k:
            count += 60
            continue
        for c in range(60):
            if c // 10 == k:
                count += 1
            elif c % 10 == k:
                count += 1

print(count)

# n, k = map(int, input().split())

# count = 0

# for a in range(n+1):
#     for b in range(60):
#         for c in range(60):
#             if str(k) in str(a) + str(b) + str(c):
#                 count += 1

# print(count)
