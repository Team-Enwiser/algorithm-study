#2178

from collections import deque

n, m = map(int, input().split())
iList = [list(input()) for _ in range(n)]


count1 = 1
count2 = 0
result = 1
move = [-1, 1]

queue = deque([(0, 0)])
iList[0][0] = '0'
while queue:
    v = queue.popleft()
    #print(v)
    for i in move:
        if 0 <= v[0]+i < n:
            if iList[v[0]+i][v[1]] == '1':
                queue.append((v[0]+i, v[1]))
                iList[v[0]+i][v[1]] = '0'
                count2 += 1
                #show()
    for i in move:
        if 0 <= v[1]+i < m:
            if iList[v[0]][v[1]+i] == '1':
                queue.append((v[0], v[1]+i))
                iList[v[0]][v[1]+i] = '0' 
                count2 += 1
                #show()
    
    if iList[n-1][m-1] == '0':
        result += 1
        break
    
    #탐색한 거리.
    count1 -= 1
    if count1 == 0:
        #print()
        result += 1
        count1 = count2
        count2 = 0
print(result)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
maze = [input() for _ in range(N)]


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    q = deque()
    q.append((0, 0, 1))
    while q:
        y, x, d = q.popleft()

        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx] and maze[ny][nx] == '1':
                chk[ny][nx] = True
                q.append((ny, nx, nd))


print(bfs())