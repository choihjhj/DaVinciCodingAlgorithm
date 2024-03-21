'''
이 문제는 최소칸 수를 찾으라는 문제기 때문에 BFS로 풀어야 한다. 대부분 최소라는 단어가 있으면 BFS로 풀면 된다.
문자열로 확인할 것이고, visited로 칸수를 증가하며 (N,M)애 도달했을 때의 visited 결과값인 칸수를 체크할 것이다.
'''
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
