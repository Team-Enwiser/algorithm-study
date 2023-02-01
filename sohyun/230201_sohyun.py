
# string length
some_string = "Hello World"
print(len(some_string))
# some_string[:::]= 
print(some_string[::-1])  # reverse

# strings are immutable  
# 문자열 자체를 바꿀 수 없다. 

# string function
func = "python is easy programming language"
print(func.count('p'))  # 2

print(func.find('p'))  # 0  첫 번째 p의 위치

comma = ","
func = comma.join('python')
print(func)  # p,y,t,h,o,n

print(func.split(',')) 

python_is_easy = "python is easy"
print(python_is_easy.split())  

# 공백 제거
some_string = "    computer     "
print(some_string.strip())  # lstrip, rstrip 각각 왼쪽, 오른쪽 공백 제거

# validator
str = "python"
print(str.isalnum()) # alpha or num
print(str.isalpha()) # only alpha
print(str.isdigit()) # only digit
print(str.islower()) # only lower
print(str.isupper()) # only upper

# formatting
print("I have a {}, and I have an {}".format("pen", "apple"))
print("I have a {0}, and I have an {1}".format("pen", "apple"))


user_name = "sohyun"
password="asdfasdf"
print(f"Hello, {user_name}! Your password is {password}")


# # 1번
# telephone = input("전화번호를 입력하세요: ")
# temp = telephone.split(' ')
# result = "-".join(temp)
# print(result)

# # 2번
# string = input()
# if(string.isalnum()):
#     print("isalnum True")
# if(string.isalpha()):
#     print("isalpha True")
# if(string.isdigit()):
#     print("isdigit True")
# if(string.islower()):
#     print("islower True")
# if(string.isupper()):
#     print("isupper True")



# list
lang = []
lang.append("python")

# 특정한 위치에 원하는 값 추가
lang.insert(1, "java")
print(lang)
# lang.remove("python")
print(lang)
lang.pop(1)  
print(lang)


# 정렬
numbers = [1, 3, 5, 2, 4]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

# reverse sort
numbers.sort(reverse=True)
print(numbers)
 
index_of_two = numbers.index(2) # find index of 2
print(index_of_two)


# 배열 합치기
numbers += [5, 6]
print(numbers)
numbers.extend([7, 8])
print(numbers)

# 
if 'cat' in ['dog', 'cat', 'fox']:
    print("cat is in the list")


# tuple
tuple1 = (1, 2, 3, 4)

# 삭제나 추가가 불가능

# 더하거나 반복하는 것은 가능
print(tuple1 * 3)

# 값을 편하게 바꿀 수 있다
# 혹은 함수에서 하나 이상의 값을 반환할 때 사용

def quot_and_rem(x, y):
    quot = x // y
    rem = x % y
    return (quot, rem)

(quot, rem) = quot_and_rem(5, 2)

# list <-> tuple
list((1,2))
tuple([1,2])

animals = ['rabbit', 'cat', 'dog', 'aligator', 'tiger', 'lion']
animals.append("bear")
animals += ["monkey", "elephant"]
animals.sort(reverse=True)
print(animals)
even_animals = animals[::2]
print(even_animals)

# dictionary 
dict1 = {"age": 20, "name": 'sohyun'}
#  추가 
dict1['name'] = 'sohyun'
#value 값은 어떤 자료형이든 가능

# 삭제 
# del dict1['name']

# key만 출력
print(dict1.keys())

# value만 출력
print(dict1.values())

# key, value 쌍으로 출력
print(dict1.items())
# dict1['name'] 은 안된다.  
print(dict1.get('name',0))
dict1.setdefault('english',[])
print(dict1.get('english',0))
print(dict1['english'])

money = 10000
if money > 10000:
  print("good")
elif money > 5000:
  print("not bad")
else:
  print("bad")


import random
answer = random.randint(1, 100)
print(answer)
guess= int(input("guess the number: "))
if guess == answer:
  print("correct")
else:
  print("wrong")

print('good') if money > 10000 else print('bad')
str = "good" if money > 10000 else "bad"
print(str)

num = int(input("input number: "))

def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)


def mul_sum(*args):
  sum = 0
  for i in args:
    sum += i
  return sum
print(mul_sum(1,2,3,4,5))

# list comprehension
old_list =[1,2,3,4,5]
double_list=[i*2 for i in old_list if i%2 == 0]
print(double_list)