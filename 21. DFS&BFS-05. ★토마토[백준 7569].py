''' 
이건 3차원 리스트 문제고, 앞뒤까지 있어 주의해야하는 문제!
d=[(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)] #상하좌우앞뒤 
방향셋팅이 중요!
1을 찾아 주위의 0을 익혀가는 3차원 리스트 문제, [백준7576번 토마토 문제] 2차원 리스트의 상위 버전 문제임
'''
import sys
from collections import deque
M,N,H=map(int, sys.stdin.readline().rstrip().split()) #가로,세로,상자수
d=[(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)] #상하좌우앞뒤
dq=deque()
arr=[]
for i in range(H):
    temp=[]
    for j in range(N):
        row=list(map(int, sys.stdin.readline().rstrip().split()))
        for k in range(M):
            if row[k]==1:
                dq.append((i,j,k))
        temp.append(row)
    arr.append(temp) #2차원 리스트를 append해서 3차원 리스트로 만들기
def bfs():
    while dq:
        i,j,k=dq.popleft()
        for p in range(6):
           ni=i+d[p][0] 
           nj=j+d[p][1]
           nk=k+d[p][2]
           if (0<=ni<H and 0<=nj<N and 0<=nk<M) and arr[ni][nj][nk]==0:
               arr[ni][nj][nk]=arr[i][j][k]+1
               dq.append((ni,nj,nk))
bfs()
def get_day():
    result=0
    for i in range(H):
        for row in arr[i]:
            if 0 in row:
                return -1
            maxx=max(row)
            if result<maxx: result=maxx
    return result-1
print(get_day())
