import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input().rstrip())
chon1,chon2=map(int, input().rstrip().split())
m=int(input().rstrip())
visited=[-1]*(n+1)
arr=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int, input().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

def DFS(node):
    if node==chon1: return
    for next_node in arr[node]:
        if visited[next_node]==-1:
            visited[next_node]=visited[node]+1
            DFS(next_node)

def BFS(node):
    dq=deque()
    dq.append(node)
    visited[node]=0
    while dq:
        v=dq.popleft()
        if v==chon1: return
        for next_node in arr[v]:       
            if visited[next_node]==-1:
                visited[next_node]=visited[v]+1
                dq.append(next_node)
    return -1

visited[chon2]=0
DFS(chon2)

# BFS(chon2)
print(visited[chon1])
