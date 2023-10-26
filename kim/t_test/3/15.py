#4673

li = []

for i in range(1, 10000):
    a = i + i//1000 + i//100%10 + i//10%10 + i%10
    li.append(a)

a = list(set(li))

b = [i for i in range(1, 10000) if i not in a]

for i in b:
    print(i)