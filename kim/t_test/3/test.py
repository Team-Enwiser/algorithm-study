# inputList = [1, 2]
# a = [i for i in range(1, 10) if i not in inputList]
# print(a)
# i = 245
# i//1000 + i//100%10 + i//10%10 + i%10
# print(i//1000)
# print(i//100%10)
# print(i//100)
# print(i//10%10)
# print(i%10)
# from collections import deque

# nL = [str(i) for i in range(100, 1000)]
# nL2 = []

# for i in nL:
#     li = list(i)
#     if li[0] == li[1] or li[0] == li[2] or li[1] == li[2]:
#         nL2.append(i)

# fL = [i for i in nL if i not in nL2]

# print(fL)

n = int(input())
iL = []

for i in range(n):
    a, b, c = map(int, input().split())
    li = [a, b, c]
    iL.append(li)
    
li = list("104")


delete = []
for j in iL:
    print(j[0], j[1], j[2])
    jli = list(str(j[0]))

    count1 = 0
    count2 = 0
    for k in range(3):

        if li[k] == jli[k]:
            count1 += 1
            print(f"count1 {count1}")
        elif li[k] == jli[0] or li[k] == jli[1] or li[k] == jli[2]:
            count2 += 1
            print(f"count2 {count2}")
        if count1 != j[1] and count2 != j[2]:
            delete.append("324")
    print(count1)
    print(count2)
    print(delete)
    print()

