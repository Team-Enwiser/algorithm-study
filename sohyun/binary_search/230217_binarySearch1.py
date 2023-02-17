# 떡볶이 떡 만들기

# n: 떡의 개수 , m: 요청한 떡의 길이
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
buy_len = 0

for i in range(1, len(arr)):
    h = arr[i]
    for i in range(len(arr)):
        if arr[i] > h:
            buy_len += arr[i] - h
    if buy_len >= m:
        break
    buy_len = 0
print(h)
