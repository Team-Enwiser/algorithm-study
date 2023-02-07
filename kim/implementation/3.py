inputList = list(input())

numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

inputStrList = [i for i in inputList if i not in numList]
inputNumList = [i for i in inputList if i in numList]

print(''.join(sorted(inputStrList)+sorted(inputNumList)))