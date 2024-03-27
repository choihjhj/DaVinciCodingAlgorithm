'''
이 문제는 최소칸 수를 찾으라는 문제기 때문에 BFS로 풀어야 한다. 대부분 최소라는 단어가 있으면 BFS로 풀면 된다.
문자열로 확인할 것이고, visited로 칸수를 증가하며 (N,M)애 도달했을 때의 visited 결과값인 칸수를 체크할 것이다.
시작점(0,0) 끝점(N,M) 결과가 궁금한 것이므로 이중포문 필요 x, 전부 bfs()로 순회해서 결과 저장해놓고 마지막칸만 확인하면 되니까
'''
# 풀이1) visited 사용, 	34052kb	76ms
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
visited = [[-1] * M for _ in range(N)]
def bfs():    
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if (0 <= nx < N and 0 <= ny < M) and arr[nx][ny] == '1' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

bfs()
print(visited[N-1][M-1])

# 풀이2) visited 사용 X ,34072kb	84ms
import sys
from collections import deque
input=sys.stdin.readline
d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
N,M=map(int, input().rstrip().split())
arr= [ list(map(int,input().rstrip())) for _ in range(N)]
def BFS():
    arr[0][0]=1
    dq=deque()
    dq.append((0,0))
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+d[i][0]
            ny=y+d[i][1]
            if(0<=nx<N and 0<=ny<M) and arr[nx][ny]==1:
                arr[nx][ny]=arr[x][y]+1
                dq.append((nx,ny))
BFS()
print(arr[N-1][M-1])
