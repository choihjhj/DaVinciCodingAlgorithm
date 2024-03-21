'''아래는 visited 리스트 사용함. 근데 이 문제는 0바다 1섬이므로 방문리스트 필요없이 그냥 방문했을 때는 1을 0으로 바꿔주면 됨'''
# DFS 풀이1
import sys
sys.setrecursionlimit(10 ** 4) #재귀쓸 때 널기
d=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] #하부터 시계반대방향으로 순회, 하 대각선 우 대각선 상 대각선 좌 대각선
def dfs(x, y):
    arr[x][y]=0
    for i in range(8):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if (0<= nx < h and 0<= ny < w) and arr[nx][ny]: #범위안에 들고, arr[nx][ny]==1이면 다음위치 탐색
                dfs(nx, ny)
  
while True:
  w,h=map(int, sys.stdin.readline().rstrip().split())
  if w==0 and h==0: 
    break
  cnt=0
  arr=[ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)] #visited 사용안할거면(값변경) list(list())로 하기, visited+list(tuple())
  for i in range(h):
    for j in range(w):
      if arr[i][j] :  
            dfs(i,j)
            cnt+=1
  print(cnt)


# BFS 풀이1
import sys
from collections import deque
d=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] #하부터 시계반대방향으로 순회 ,하 대각선 우 대각선 상 대각선 좌 대각선
def bfs(x, y):
    arr[x][y]=0
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if (0<= nx < h and 0<= ny < w) and arr[nx][ny]:
                    arr[nx][ny]=0
                    que.append((nx, ny))
  
while True:
  w,h=map(int, sys.stdin.readline().rstrip().split())
  if w==0 and h==0: 
    break
  cnt=0
  arr=[ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h) ]
  for i in range(h):
    for j in range(w):
      if arr[i][j]:  
            bfs(i,j)
            cnt+=1
  print(cnt)

'''-------------------------------------------------------------------------------------------------------------------'''
# DFS 풀이2
import sys
sys.setrecursionlimit(10 ** 4) #재귀쓸 때 널기
d=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] #하부터 시계반대방향으로 순회, 하 대각선 우 대각선 상 대각선 좌 대각선
def dfs(x, y):
    visited[x][y]=True
    for i in range(8):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if (0<= nx < h and 0<= ny < w):
            if not visited[nx][ny] and arr[nx][ny]: # visited[nx][ny]==False 이고, arr[nx][ny]==1이면 다음위치 탐색
                dfs(nx, ny)
  
while True:
  w,h=map(int, sys.stdin.readline().rstrip().split())
  if w==0 and h==0: 
    break
  visited =[ [False]*(w) for _ in range(h)]
  cnt=0
  
  arr=[ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if arr[i][j] and not visited[i][j]:  # visited[i][j]==False 이고, arr[i][j]==1이면 탐색 후 cnt 섬증가
            dfs(i,j)
            cnt+=1
  print(cnt)

# BFS 풀이2
import sys
from collections import deque
sys.setrecursionlimit(10 ** 4)
d=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] #하부터 시계반대방향으로 순회 ,하 대각선 우 대각선 상 대각선 좌 대각선
def bfs(x, y):
    visited[x][y]=True
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if (0<= nx < h and 0<= ny < w):
                if not visited[nx][ny] and arr[nx][ny]: # visited[nx][ny]==False 이고, arr[nx][ny]==1이면 다음위치 탐색
                    visited[nx][ny]=True
                    que.append((nx, ny))
  
while True:
  w,h=map(int, sys.stdin.readline().rstrip().split())
  if w==0 and h==0: 
    break
  visited =[ [False]*(w) for _ in range(h)]
  cnt=0
  
  arr=[ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if arr[i][j] and not visited[i][j]:  # visited[i][j]==False 이고, arr[i][j]==1이면 탐색 후 cnt 섬증가
            bfs(i,j)
            cnt+=1
  print(cnt)
