s = input()
result = int(s[0])
i = 1
while True:
  result *= int(s[i])
  if(result == 0 or result == int(s[i])):
    result += int(s[i])
  i += 1
  if(i == len(s)): break
print(result)
