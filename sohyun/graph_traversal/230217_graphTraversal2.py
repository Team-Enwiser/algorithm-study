# 미로 탈출
from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
queue.append((0,0))

while queue:
    x, y= queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))


print(graph[n-1][m-1])
    
