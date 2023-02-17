# 떡볶이 떡 만들기 (이진탐색)

# n: 떡의 개수 , m: 요청한 떡의 길이
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
buy_len = 0
result = [] 
while start <= end:
    mid = (start + end) // 2
    for a in arr:
        if a > mid:
            buy_len += a - mid
    if buy_len >= m:
        result.append(mid)
        start = mid + 1
    else:
        end = mid - 1
    buy_len = 0

print(max(result))