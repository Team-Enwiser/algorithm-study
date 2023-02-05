space_size = 5
direction = 'R R R U D D'

direction.split(' ')
space = [[0 for _ in range(space_size)] for _ in range(space_size)]

# L R U D
x = 0
y = 0
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
move = []

# example: L = dx[0], dy[0]
for i in range(len(direction)):
    if direction[i] == 'L':
        move.append(0)
    if direction[i] == 'R':
        move.append(1)
    if direction[i] == 'U':
        move.append(2)
    if direction[i] == 'D':
        move.append(3)

print(move)
# Loop for move
for m in move:
    # Don't get out of bound
    if x+dx[m] >= 0 and y+dy[m] >= 0:
        x = x+dx[m]
        y = y+dy[m]
        
print(y+1,x+1)

