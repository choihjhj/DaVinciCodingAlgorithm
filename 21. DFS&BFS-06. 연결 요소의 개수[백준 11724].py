# 풀이1) DFS
import sys
sys.setrecursionlimit(10**4)
N, M = map(int, sys.stdin.readline().rstrip().split()) #노드개수, 간선개수
arr=[[] for _ in range(N+1)] #맨앞 빈배열[]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().rstrip().split())
  arr[u].append(v)
  arr[v].append(u)
def dfs(node):
    visited[node] = True
    for next_node in arr[node]:
        if not visited[next_node]:
            dfs(next_node)
cnt=0
visited = [False] * (N + 1)
for i in range(1,N+1):
  if not visited[i]:
    dfs(i)
    cnt+=1
print(cnt)

# 풀이2) BFS
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split()) #노드개수, 간선개수
arr=[[] for _ in range(N+1)] #맨앞 빈배열[]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().rstrip().split())
  arr[u].append(v)
  arr[v].append(u)
  
def bfs(node):
  dq=deque([node])
  visited[node] = True
  while dq:
    v=dq.popleft()
    for next_node in arr[v]:
        if not visited[next_node]:
            dq.append(next_node)
            visited[next_node]=True
          
cnt=0
visited = [False] * (N + 1)
for i in range(1,N+1):
  if not visited[i]:
    bfs(i)
    cnt+=1
print(cnt)
