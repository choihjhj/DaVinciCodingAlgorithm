import sys
sys.setrecursionlimit(10**4)
N=int(input())
d = [(-1,0), (1,0), (0,-1), (0,1)]
arr=[list(input()) for _ in range(N)]
def dfs(x,y):
    arr[x][y]='0'
    cnt=1
    for i in range(4):
        nx=x+d[i][0]
        ny=y+d[i][1]
        if (0<=nx<N and 0<=ny<N) and arr[nx][ny]=='1':
            cnt+=dfs(nx,ny)           
    return cnt

result=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]=='1':
            result.append(dfs(i,j))            
print(len(result), *sorted(result), sep='\n')
