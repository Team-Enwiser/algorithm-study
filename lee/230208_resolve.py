
# Greedy
# 문제 2 재풀이: 1 case 추가 or input을 int로 받아서 <= 1 이면 더하기
input = '02984'
# input = '567'

result = 1
for i in range(len(input)):
    if input[i] == '0':
        continue
    elif input[i] == '1':
        result += 1
    else:
        result *= int(input[i])
print(result)

# 문제 3 재풀이: 오름차순 정렬! 왜냐면 최대한 많은 그룹을 만들어야하니까
count = 5
guild = '2 3 1 2 2'

guild = list(map(int, guild.split(' ')))
guild.sort()  # 1 2 2 2 3
member_count = 0
group = 0

for i in range(count):
    member_count += 1
    if guild[i] <= member_count:
        group += 1
        member_count = 0
print(group)
