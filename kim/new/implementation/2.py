dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

input = list(input())

x = int(input[1])
y = ord(input[0])-96

result = 0

for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        result += 1

print(result)