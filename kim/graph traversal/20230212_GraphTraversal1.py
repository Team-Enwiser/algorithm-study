from collections import deque

#n, m = map(int, input().split())
n = 4
m = 5
#iList = [list(input()) for _ in range(n)]
iList = [['0', '0', '1', '1', '0'], ['0', '0', '0', '1', '1'], ['1', '1', '1', '1', '1'], ['0', '0', '0', '0', '0']]
result = 0

move = [-1, 1]

#print(iList)

for a in range(n):
    for b in range(m):
        if iList[a][b] == '0':
            result += 1
            #print()
            #print(result)
            queue = deque([(a, b)])
            #print(queue)
            iList[a][b] = '1'

            while queue:
                #print(queue)
                v = queue.popleft()
                #print(v, end=' ')
                   
                for i in move:
                    #위, 아래 탐색
                    if 0 <= v[0]+i < n:
                        if iList[v[0]+i][v[1]] == '0':
                            queue.append((v[0]+i, v[1]))
                            iList[v[0]+i][v[1]] = '1'
                for i in move:
                    #왼, 오른쪽 탐색
                    if 0 <= v[1]+i < m:
                        if iList[v[0]][v[1]+i] == '0':
                            queue.append((v[0], v[1]+i))
                            iList[v[0]][v[1]+i] = '1'

#print(iList)
print(result)

# def aa():
#     queue = deque([(1, 10), (2, 1)])
#     queue.append((1, 2))
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         print(v[1])

# aa()