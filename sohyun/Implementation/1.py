n = int(input())
plan = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
nx, ny = 0, 0

for p in plan:
  if p == "L":
    if ny != 0:
      ny += dy[0]
  if p == "R":
    if ny != n-1:
      ny += dy[1]
  if p == "U":
    if nx != 0:
      nx += dx[2]
  if p == "D":
    if nx != n-1:
      nx += dx[3]

print(nx+1, ny+1)