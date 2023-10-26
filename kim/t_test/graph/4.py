#1743

from collections import deque

n, m, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0

for a in range(n):
    for b in range(m):
        count = 0
        if arr[a][b] == 1:
            count += 1
            queue = deque([(a, b)])
            arr[a][b] = 0

            while queue:
                v = queue.popleft()
                for i in range(4):
                    xx = v[0] + dx[i]
                    yy = v[1] + dy[i]
                    if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 1:
                        count += 1
                        arr[xx][yy] = 0
                        queue.append((xx, yy))

            if count > result : result = count

print(result)