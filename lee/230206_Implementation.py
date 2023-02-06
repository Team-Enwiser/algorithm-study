# example
'''
[문제]

여행가 A는 N × N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 × 1 크기의 정사각형으로 나누어져 있습니다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.

 

계획서에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있습니다. 각 문자의 의미는 다음과 같습니다

L: 왼쪽으로 한 칸 이동

R: 오른쪽으로 한 칸 이동

U: 위로 한 칸 이동

D: 아래로 한 칸 이동

이때 여행가 A가 N × N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다. 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됩니다 다음은 N = 5인 지도와 계획서입니다.

[입력]

5

R R R U D D

[출력]

3 4
'''

# 1 시각
# H hour M minute S second
# if input is 3, 13 hour case is fully true
# per 1 hour, 60 minute + 60 second, totally 3600 case exist
# true case:
# 3 hour, 13 hour
# 03,13,23,33,43,53 min
# 30,31,32,33,34,35,36,37,38,39 min
# 33 is duplicate, total 15

# so except 3,13 hour, 15*60 + 45*15 case in each hour
# print(15*60 + 45*15)

# code
input = 5

result = 0
for h in range(input+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                result += 1
print((15*60 + 45*15)*5 + 3600)  # = 11475
print(result)

# 2 왕실의 나이트
'''
[문제]

행복 왕국의 왕실 정원은 체스판과 같은 8 × 8 좌표 평면입니다. 
왕실 정원의 특정한 한 칸에 나이트가 서있습니다. 
나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 
정원 밖으로는 나갈 수 없습니다

나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.

1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

8 × 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 
나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요. 
왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 
열 위치를 표현할 때는 a 부터 h로 표현합니다.

c2에 있을 때 이동할 수 있는 경우의 수는 6가지입니다
a1에 있을 때 이동할 수 있는 경우의 수는 2가지입니다

[입력]

a1

[출력]

2
'''
'''
 a b c d e f g h
1
2
3
4
5
6
7
8
'''
input = 'a1'
# input = 'c2'

# ratate by clock moving from 11 hour to 10 hour
dy = [-2, -2, -1, 1, 2, 2, 1, -1]
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
board = [[0 for _ in range(8)] for _ in range(8)]
x = ord(input[0])-ord('a')
y = int(input[1]) - 1
result = 0

for n in range(8):
    if y+dy[n] >= 0 and x+dx[n] >= 0:
        result += 1
print(result)
# chr()

# 3 문자열 재정렬
'''
[문제]

알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출련한 뒤에, 
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다. 

예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

[입력]

K1KA5CB7

[출력]

ABCKK13
'''
input = 'K1KA5CB7'

alpha = []
num = 0
for i in input:
    if i.isupper():
        alpha.append(i)
    else:
        num += int(i)
alpha.sort()
result = ''.join(alpha) + str(num)

print(result)
