n, m = map(int, input().split())
sortList = [list(input().split()) for _ in range(2)]

for _ in range(m):
    sortList[0].sort()
    sortList[1].sort()
    
    if sortList[0][0] >= sortList[1][n-1]:
        break
    else:
        sortList[0][0], sortList[1][n-1] = sortList[1][n-1], sortList[0][0]

    print(sortList[0])    

print(sum(map(int, sortList[0])))