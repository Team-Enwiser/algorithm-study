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