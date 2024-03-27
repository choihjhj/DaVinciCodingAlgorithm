''' DFS 문제, 1번 컴터에 연결된 바이러스 컴터 개수니까 DFS(1)-1 자기자신은 빼줘야함
만약, 4번 컴터에 연결된 컴터 수 라면 DFS(4)-1
'''
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=int(input().rstrip())
M=int(input().rstrip())
visited=[0]*(N+1)
arr=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int, input().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

def DFS(node):
    visited[node]=1
    cnt=1
    for i in arr[node]:
        if not visited[i]:
            cnt+=DFS(i)
    return cnt

def BFS(node):
    visited[node]=1
    cnt=1
    dq=deque()
    dq.append(node)
    while dq:
        for i in arr[dq.popleft()]:
            if not visited[i]:
                visited[i]=1
                dq.append(i)
                cnt+=1
    return cnt

print(DFS(1)-1)
# print(BFS(1)-1)
