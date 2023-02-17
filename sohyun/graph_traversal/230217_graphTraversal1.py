# 음료수 얼려 먹기
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
result = 0


def dfs(graph, x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x, y - 1)
        dfs(graph, x + 1, y)
        dfs(graph, x - 1, y)
        dfs(graph, x, y + 1)
        return True
    return False


for i in range(len(graph)):
    for j in range(len(graph[0])):
        if dfs(graph, i, j):
            result += 1

print(result)
