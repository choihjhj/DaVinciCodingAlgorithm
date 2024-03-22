'''
DFS는 [x][y]=0, for문, 재귀로 호출
BFS는 deque, while문+방향순회for문, [x][y]=0,[nx][ny]=0 처리 큐에 popleft, append
섬개수 세는 문제는 main에서 이중포문돌때 cnt+=1하면 됨(백준 4963 섬의개수 문제)
만약 섬안의 집수까지 세는건 dfs함수에서 cnt=1만들고 재귀로 cnt+=dfs(nx,ny)해서 최종 return cnt 하면 됨(백준 2667 단지번호붙이기 문제)
'''
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
