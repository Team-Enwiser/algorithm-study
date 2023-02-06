n, k = map(int, input().split())
# 1번: -1, 2번: k로 나누기, 단 n이 k로 나누어 떨어질 때만 가능
count = 0
while(n != 1):
  if(n % k == 0):
    n //= k
  else:
    n -= 1
  count += 1
print(count)