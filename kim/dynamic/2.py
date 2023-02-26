n = 26
d = [0] * (n+1)
min = 1000

def ho(x):
    if x == 1:
        return 1
    
    #if 정수가 아니면:
    # return NULL 

    if d[x] != 0:
        return d[x]
    
    counter += 1
    d[x] = min(ho(x//5), ho(x//3), ho(x//2), ho(x-1))
    
    # if x // 5 == 0:
    #     ho(x//5)
    #     d[x] += 1
    # if x // 3 == 0:
    #     ho(x//3)
    #     d[x] += 1
    # if x // 2 == 0:
    #     ho(x//2)
    #     d[x] += 1
    # ho(x-1)