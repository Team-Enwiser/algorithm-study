import heapq
INF = int(1e9)
# 노드 개수 n, 간선 개수 m, 시작 노드 c
n, m, c = map(int, input().split())

city = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  x, y, z = map(int, input().split())
  city[x].append((y, z))

q = []
# 시작 노드의 최단 거리 초기화
distance[c] = 0
heapq.heappush(q, (0, c))

while q:
  dist, now = heapq.heappop(q) # 현재 노드의 최단 거리와 번호
  if distance[now] < dist:
    continue
  
  for i in city[now]:
    cost = dist + i[1]  # 거쳐가는 비용 계산
    if distance[i[0]] > cost:
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))

# 무한인 거리 제거(방문하지 않은 노드의 거리 삭제) 
distance.remove(INF)
# 메시지를 받는 도시의 총 개수, 총 걸리는 시간 
print(len(distance) - 1, max(distance)) # 시작 노드가 개수에 포함됨 -> -1