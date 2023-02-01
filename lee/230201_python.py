# print('Hello World!')
# print('Hello python!')

def juhyeong():
	# input
	# name = input("What is your name? ") 
	# print("Hi, ", name)

	# type casting
	# int(input("How old are you? "))

	# String 
	# some_string = "python" 
	# print(len(some_string))
	# print(some_string[::-1])
	# similar for in C

	# func = "python is easy programming language" 
	# print(func.count('p')) # 2
	# print(func.find('p')) # 0
	
	# comma = ","
	# func = comma.join('python')
	# print(func)
	
	# print(func.split(','))

	# python_is_easy = "python is easy" 
	# print(python_is_easy.split())

	# some_string = " computer " 
	# print(some_string.strip()) # lstrip rstrip

	# str = '123asdASD'
	# print(str.isalnum()) # alpha & num
	# print(str.isalpha()) # only alpha
	# print(str.isdigit()) # only number
	# print(str.islower()) # only lower case
	# print(str.isupper()) # only upper case

	# print("I have a {}, I have an {}.".format("pen", "apple")) # pen apple
	# print("I have a {0}, I have an {1}.".format("pen", "apple")) # pen apple
	# print("I have a {0}, I have an {0}.".format("pen", "apple")) # pen pen

	# user_name = 'johndoe'
	# password = '1q2w3e4r'
	# print(f"Hello, {user_name}! Your password is {password}")

	#1. 사용자가 입력한 전화번호를 저장하려합니다. 전화번호의 구분자로 - 또는   를 혼합하 여 사용할 때 이를 split과 join을 이용하여 - 로 통일하여 입력 받아 결과물을 출력하세 요.
	#2. 사용자가 다음과 같은 입력을 할때, 그 자료가 알파벳 단독인지, 숫자 단독인지, 알파벳 숫자인지, 소문자인지, 대문자인지를 formating 하여 출력하세요

	# lang = []
	# lang.append('123')
	# print(lang)
	# lang.insert(0, "c")
	# print(lang)
	# # lang.remove("123")
	# # print(lang)
	# java = lang.pop()
	# print(java)

	# numbers = [2, 1, 4, 3] 
	# print(numbers)
	# numbers.sort() 
	# print(numbers)

	# numbers = [2, 1, 4, 3] 
	# numbers.reverse()
	# print(numbers)

	# numbers = [2, 1, 4, 3] 
	# index_of_two = numbers.index(2) # find
	# print(index_of_two)
	# print(numbers[2]) # 0 1 2 order

	# numbers = [2, 1, 4, 3] 
	# numbers += [5, 6] # same extend
	# print(numbers) 
	# numbers.extend([7, 8]) # same +=
	# print(numbers)

	# if 'cat' in ['fox', 'dog', 'cat']:
	# 	print('cat')

	# tuple1 = (1, 2, 3, 4)
	# del tuple[1] 
	# tuple1[1] = 'c'

	# def quot_and_rem(x,y): 
	# 	quot = x // y
	# 	rem = x % y
	# 	return (quot, rem)
	# (quot, rem) = quot_and_rem(3,10)
	# print(quot, rem)

	# dict1 = {'name':'lee'}
	# dict1['english'] = "pass"
	# print(dict1['english'])
	# print(dict1)

	# print(dict1.keys())
	# print(dict1.values())
	# print(dict1.items())

	# dict1 = {'name':'lee'}
	# dict1['english'] = "pass"
	# test = dict1.pop('name')
	# print(test)

	# dict1 = {'name':'lee'}
	# print(dict1.get('english', 0))
	# print(dict1.setdefault('english',[]))
	# print(dict1)
	# dict1.get('english')
	# dict1['english']

	# money = 10000
	# if money > 10000:
	# 	print('good')
	# elif money >= 5000:
	# 	print('soso')
	# else:
	# 	print('bad')

	# money = 10000
	# if money > 10000:
	# 	print('good')
	# else:
	# 	print('bad')

	# print('good') if money > 10000 else print('bad')
	# str = 'good' if money > 10000 else 'bad'
	
	# for i in ["python", "java", "golang"]: 
	# 	print(i)

	# for i in "python":
	# 	print(i)

	# sum = 0
	# # range(0,10)
	# for i in range(1,11):
	# 	sum += i 
	# 	sum = sum + i
	# print(sum)

	# def mul_return(a): 
	# 	b=a+1
	# 	return a,b
	# x,y = mul_return(1)
	# print(x,y)

	old_list = [1, 2, 3, 4, 5,]
	doubled_list = [] 
	# for i in old_list:
	# 	doubled_list.append(i * 2)
	# print(doubled_list)

	# doubled_list = [i * 2 for i in old_list] 
	# print(doubled_list)

	# for i in old_list:
	# 	if i % 2 ==0:
	# 		doubled_list.append(i * 2)
	
	# doubled_list = [i * 2 for i in old_list if i % 2 ==0] 
	# print(doubled_list)

	# 1~100까지 리스트로 더하세요
	# n = [[0 for _ in range(10)] for _ in range(10)]
	# print(n)
	pass

juhyeong()