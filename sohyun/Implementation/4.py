#[문제] 문자열 재정렬
s = input()

alpha = ''
sum = 0
for i in s:
    if i.isalpha():
        alpha += i
    else:
       sum += int(i)

print(''.join(sorted(alpha)) + str(sum)) 