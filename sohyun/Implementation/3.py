# [문제] 왕실의 나이트
c = input()

# 수평2 수직1, 수직2,수평1
dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

count = 0
x = int(c[1]) - 1
y = ord(c[0]) - 97

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue
    count += 1

print(count)