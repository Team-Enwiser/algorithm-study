#2583

from collections import deque

n, m, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

for i in arr:
    print(i)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = []

for a in range(n):
    for b in range(m):
        count = 0
        if arr[a][b] == 0:
            count += 1
            queue = deque([(a, b)])
            arr[a][b] = 1

            while queue:
                v = queue.popleft()
                for i in range(4):
                    xx = v[0] + dx[i]
                    yy = v[1] + dy[i]
                    if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:
                        count += 1
                        arr[xx][yy] = 1
                        queue.append((xx, yy))

            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i, end = ' ')