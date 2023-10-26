from collections import Counter

a = int(input())

fearL = list(map(int, input().split()))

fearL.sort()
   
b = dict(Counter(fearL))

less = 0

result = 0

for i in b.keys():
    result += (b[i]+less)//i
    less = (b[i]+less)%i

print(result)