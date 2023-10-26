#11724

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)

ans = 0
chk = [False] * N


def dfs(now):
    for nxt in adj[now]:
        if not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)