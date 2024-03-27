import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M=map(int, input().rstrip().split())
visited=[0]*(N+1)
arr=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int, input().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)
  
def DFS(node):
    visited[node]=1
    for i in arr[node]:
        if not visited[i]:
            DFS(i)    

def BFS(node):
    visited[node]=1
    dq=deque()
    dq.append(node)
    while dq:
        for i in arr[dq.popleft()]:
            if not visited[i]:
                dq.append(i)
                visited[i]=1    

cnt=0
for i in range(1,N+1):
    if not visited[i]: 
        DFS(i)
        # BFS(i)
        cnt+=1    
print(cnt)
