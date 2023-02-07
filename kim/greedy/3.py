# 각 공포도의 사람들 수를 내고, 낮은 공포도부터 그 공포도대로 %, 남은 사람 수는 위로.
from collections import Counter

n = int(input())
fearList = list(map(int, input().split()))
fearCount = Counter(fearList)
countList = []
result = 0

for i in range(n):
    countList.append(fearCount[i+1])

for i in range(n):
    if countList[i] == 0:
        continue

    result += countList[i] // (i + 1)
    
    if(i + 1 == n):
        break
    else:
        countList[i + 1] += countList[i] % (i + 1)
    print(countList)

print(result)