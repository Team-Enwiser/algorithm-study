# [문제] 시각
n = int(input())

# 10으로 나눈 나머지가 3 or 몫이 3
result = 0

for i in range(n+1):
    if i % 10 == 3:
        result += 60 * 60
    else:
        for j in range(60):
            if j % 10 == 3 or j // 10 == 3:
                result += 60
            else:
                for k in range(60):
                    if k % 10 == 3 or k // 10 == 3:
                        result += 1
        
print(result) 