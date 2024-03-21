# DFS(깊이우선탐색)
visited = [[False] * M for _ in range(N)]
d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if (0 <= nx < N and 0 <= ny < M):
            if  not visited[nx][ny]:
                dfs(nx,ny)

dfs(0, 0)

# BFS(너비우선탐색)
from collections import deque
visited = [[False] * M for _ in range(N)]
d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
def bfs(x, y):
    visited[x][y] = True
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        for i in range(4):
           nx = x + d[i][0]
           ny = y + d[i][1]
            if (0 <= nx < N and 0 <= ny < M):
                if  not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))

bfs(0, 0)
