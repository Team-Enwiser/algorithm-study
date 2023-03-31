# #7568

# n = int(input())
# a = []

# for i in range(n):
#     x, y = map(int, input().split())
#     li = [x, y, i, 0]
#     a.append(li)

# b = sorted(a, reverse=True)
# print(b)

# count1 = 1
# count2 = 1

# for i in range(n):
#     b[i][3] = count1

#     if i == (n - 1): break

#     if b[i][0] > b[i+1][0] and b[i][1] > b[i+1][1]:
#         count1 += count2
#         count2 = 1
#     else:
#         count2 += 1

# for i in range(n):
#     b[i][0], b[i][2] = b[i][2], b[i][0]

# b.sort()

# for i in range(n):
#     if i == (n - 1):
#         print(b[i][3])
#     else:
#         print(b[i][3], end=' ')

n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    li = [x, y, 0]
    a.append(li)

for i in range(n):
    count = 1
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            count += 1
    a[i][2] = count

for i in range(n):
        print(a[i][2], end=' ')