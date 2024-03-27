import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int, input().rstrip().split())
arr=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int, input().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

def BFS(node):
    dq=deque()
    dq.append(node)
    visited=[-1]*(N+1)
    visited[node]=0
    while dq:
        v=dq.popleft()
        for i in arr[v]:
            if visited[i]==-1:
                visited[i]=visited[v]+1
                dq.append(i)
    return sum(visited[1:])

minn= float("INF")
result_idx=0
for i in range(1,N+1):
    summ=BFS(i)
    if minn>summ: #더 작은값 발견하면 minn 재셋팅, 인덱스 저장
        minn=summ
        result_idx=i
print(result_idx)
