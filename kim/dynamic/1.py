n = 10
a = [1, 3, 1, 5, 7, 1, 2, 6, 3, 2]

d = [0] * (n)

def sibal(x):
    if x == (n - 1) or x == (n - 2):
        return a[x]
    if x == n:
        return 0

    if d[x] != 0:
        print("index :", x+1, "already calculated")
        return d[x]
    
    d[x] = a[x] + max(sibal(x+2), sibal(x+3))
    
    return d[x]

print(max(sibal(0), sibal(1)))

 # i = sibal(x+2)
    # j = sibal(x+3)
    
    # if i > j:
    #     d[x] = a[x] + i
    # else:
    #     d[x] = a[x] + j
# x = sibal(0)
# y = sibal(1)
# if x > y:
#     print(x, "1 start")
# else:
#     print(y, "2 start")

'''
[1] + [3][2]
    + [3][3]



[6][0] = 3
[6][1] = 4

둘중에 큰거야
[3] = [5]와 [6]중에 더 큰거를 [3]과 더한 값. [5]는 [7]과 [8]중에 더 큰거를 [5]와 더한 값이지.

'''