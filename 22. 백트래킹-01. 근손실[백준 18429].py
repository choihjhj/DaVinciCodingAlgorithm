import sys
input=sys.stdin.readline
N, K = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
ans = 0
visited = [False] * N
def dfs(n, weight):
    global ans
    if weight < 500:
        return
    if n == N:
        ans += 1
        return
    weight -= K
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n + 1, weight + A[i])
            visited[i] = False
dfs(0, 500)
print(ans)
