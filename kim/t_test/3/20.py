n = int(input())

iL = []

for i in range(n):
    a, b, c = map(int, input().split())
    li = [a, b, c]
    iL.append(li)

nL = [str(i) for i in range(100, 1000)]
nL2 = []

for i in nL:
    li = list(i)
    if li[0] == li[1] or li[0] == li[2] or li[1] == li[2]:
        nL2.append(i)
    elif li[0] == '0' or li[1] == '0' or li[2] == '0':
        nL2.append(i)

fL = [i for i in nL if i not in nL2]
delete = []

for i in fL:
    li = list(i)

    for j in iL:
        count1 = 0
        count2 = 0
        jli = list(str(j[0]))

        for k in range(3):

            if li[k] == jli[k]:
                count1 += 1

            elif li[k] == jli[0] or li[k] == jli[1] or li[k] == jli[2]:
                count2 += 1

        if count1 != j[1] or count2 != j[2]:
            delete.append(i)

de = list(set(delete))

final = [i for i in fL if i not in de]

print(len(final))