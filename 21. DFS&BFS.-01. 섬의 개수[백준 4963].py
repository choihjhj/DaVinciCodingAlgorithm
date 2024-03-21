import sys
sys.setrecursionlimit(10 ** 4)
d=[(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)] #대각선,상,하,좌,우

def dfs(x, y):
  
while True:
  w,h=map(int, sys.stdin.readline().rstrip().split())
  check=[ [False]*(w) for _ in range(h)]
  cnt=0
  if w==0 and h==0: 
    break
  arr=[ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if arr[i][j]==1:
        dfs(i,j)
        cnt+=1
  print(cnt)
  
  
