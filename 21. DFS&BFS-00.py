# DFS(깊이우선탐색)
visited = [[False] * M for _ in range(N)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
def dfs(y, x):
    print(y, x)
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < N and 0 <= nx < M):
            continue
        if arr[ny][nx] == 1:
            continue
        if not visited[ny][nx]:
            dfs(ny, nx)

dfs(0, 0)

# BFS(너비우선탐색)
from collections import deque
def bfs(y, x):
    visited = [[False] * M for _ in range(N)]
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    visited[y][x] = True
    que = deque()
    que.append((y, x))

    while que:
        y, x = que.popleft()
        print(y, x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if arr[ny][nx] == 1:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx))

bfs(0, 0)
