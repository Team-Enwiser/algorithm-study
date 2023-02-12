# BS - recursive
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (end + start) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, end)

arr = [n for n in range(20) if n % 2 == 0]
target = 4
print(arr, len(arr))
result = binary_search_recursive(arr, target, 0, len(arr))

if result == 'None':
    print('No such result')
else:
    print(f"Result is {result}")


# BS - loop
def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end // 2)
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

arr = [n for n in range(20) if n % 2 == 0]
target = 4
print(arr, len(arr))
result = binary_search_loop(arr, target, 0, len(arr))

if result == 'None':
    print('No such result')
else:
    print(f"Result is {result}")

# bisect
from bisect import bisect_left, bisect_right
arr = [n for n in range(20) if n % 2 == 0]
target = 4

print(bisect_left(arr, target))
print(bisect_right(arr, target))

# bisect count
from bisect import bisect_left, bisect_right

def count_by_range(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx

arr = [n for n in range(20) if n % 2 == 0]
print(count_by_range(arr, 4, 4))
print(count_by_range(arr, -1, 3))