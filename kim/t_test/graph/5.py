#2667

from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = []

for a in range(n):
    for b in range(n):
        count = 0
        if arr[a][b] == '1':
            count += 1
            queue = deque([(a, b)])
            arr[a][b] = '0'

            while queue:
                v = queue.popleft()
                for i in range(4):
                    xx = v[0] + dx[i]
                    yy = v[1] + dy[i]
                    if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == '1':
                        count += 1
                        arr[xx][yy] = '0'
                        queue.append((xx, yy))

            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)