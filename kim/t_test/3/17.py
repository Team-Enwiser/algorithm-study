#1018

# from collections import deque

# n, m = map(int, input().split())
# iList = [list(input()) for _ in range(n)]

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# iList[0][0] = '0'
# for a in range(n-7):
#     for b in range(m-7):
#         queue = deque([(a, b)])
#         while queue:
#             v = queue.popleft()
#             #print(v)
#             for i in range(4):
#                 if a <= v[0]+dx[i] < n and b <= v[1]+dy[i] < m:
#                     if iList[v[0]+i][v[1]] == '1':
#                         queue.append((v[0]+i, v[1]))
#                         iList[v[0]+i][v[1]] = '0'
#                         count2 += 1
#                         #show()
    

#     # print(count1, end=' ')
#     # print(count2, end=' ')
#     # print(result)

n, m = map(int, input().split())
iList = [list(input()) for _ in range(n)]

even = [0, 2, 4, 6]
odd = [1, 3, 5, 7]

countL = []

for a in range(n-7):

    for b in range(m-7):
        li = iList
        count1 = 0
        count2 = 0

        for c in range(8):

            if c in even:

                for d in even:
                    if li[a+c][b+d] == 'B':
                        count1 += 1
                    else:
                        count2 += 1
                for d in odd:
                    if li[a+c][b+d] == 'W':
                        count1 += 1
                    else:
                        count2 += 1

            else:

                for d in odd:
                    if li[a+c][b+d] == 'B':
                        count1 += 1
                    else:
                        count2 += 1
                for d in even:
                    if li[a+c][b+d] == 'W':
                        count1 += 1
                    else:
                        count2 += 1

        countL.append(count1)
        countL.append(count2)

print(min(countL))
