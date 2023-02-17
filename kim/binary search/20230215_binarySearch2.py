from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
aList = list(map(int, input().split()))
a = [1,2,3,3,3,3,4,4,5,8,9]

print(aList)
def count_by_range(a, value):
    right_index = bisect_right(a, value)
    left_index = bisect_left(a, value)
    result = right_index-left_index

    if result == 0:
        return -1
    else:
        return result

print(count_by_range(aList, x))