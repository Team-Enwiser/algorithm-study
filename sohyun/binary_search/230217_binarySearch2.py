# 정렬된 배열에서 특정 수의 개수 구하기 (O(logN))
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left_idx = bisect_left(arr, x)
right_idx = bisect_right(arr, x)

if right_idx == left_idx:
    print(-1)
else:
    print(right_idx - left_idx)
