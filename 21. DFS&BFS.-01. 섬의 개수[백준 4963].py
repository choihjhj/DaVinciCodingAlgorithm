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
