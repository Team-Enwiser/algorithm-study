#2231

n = int(input())

for i in range(n + 1):
    if i == 0:continue
    a = i - i//1000000*1000000
    b = a - a//100000*100000
    c = b - b//10000*10000
    d = c - c//1000*1000
    e = d - d//100*100
    f = e - e//10*10

    x = i + i//1000000 + a//100000 + b//10000 + c//1000 + d//100 + e//10 + f
    if x == n:
        print(i)
        break
    if i == n:
        print(0)
        break