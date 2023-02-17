n, m = 4, 56#map(int, input().split())
array = [19,15,10,17]#list(map(int, input().split()))
final = []

def binary(dList, target, start, end):
    while start <= end:
        result = 0
        mid = (start + end) // 2

        for i in range(n):
            if dList[i] - mid >= 0:
                result += dList[i] - mid

        if result > target:
            start = mid + 1
            final.append(mid)
        elif result < target:
            end = mid - 1
        else:
            return mid
    
        return None    

a = binary(array, m, 1, max(array))

if a == None:
    if final == []:
        print("can't")
    else: 
        print(max(final))
else:
    print(a)