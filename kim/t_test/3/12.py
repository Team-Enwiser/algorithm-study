#1526

n = int(input())

for i in reversed(range(4, n+1)):
    li = list(str(i))
    for j in range(len(li)):
        if li[j] == '4' or li[j] == '7':
            if j == len(li)-1:
                print(i)
                exit(0)
            continue
        else:
            break