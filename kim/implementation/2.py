loc = list(input())
result = 0

moveList = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

if loc[0] == 'a':
    loc[0] = '1'
elif loc[0] == 'b':
    loc[0] = '2'
elif loc[0] == 'c':
    loc[0] = '3'
elif loc[0] == 'd':
    loc[0] = '4'
elif loc[0] == 'e':
    loc[0] = '5'
elif loc[0] == 'f':
    loc[0] = '6'
elif loc[0] == 'g':
    loc[0] = '7'
else:
    loc[0] = '8'

x = int(loc[0])
y = int(loc[1])

for i in moveList:
    if 1 <= x + i[0] <= 8 and 1 <= y + i[1] <= 8:
        result += 1

print(result)