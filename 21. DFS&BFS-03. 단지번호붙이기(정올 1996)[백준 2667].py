N = int(input())
arr = [list(input()) for _ in range(N)]
d = [(-1,0), (1,0), (0,-1), (0,1)]
def dfs(x, y):
    arr[x][y] = "0"
    cnt = 1
    for k in range(4):
        nx = x + d[k][0]
        ny = y + d[k][1]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == "1":
            cnt += dfs(nx, ny)
    return cnt

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == "1":
            cnt = dfs(i, j)
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)
