import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input().rstrip())
chon1, chon2= map(int, input().rstrip().split())
m=int(input().rstrip())
arr=[[] for _ in range(n+1)] #맨앞 빈배열[]
for _ in range(m):
  u, v = map(int, input().rstrip().split())
  arr[u].append(v)
  arr[v].append(u)
visited=[0]*(n+1)

visited[chon1]=0
def dfs(node):
  if node==chon2: return
  for next in arr[node]:		
    if not visited[next]:
      visited[next]=visited[node]+1
      dfs(next)
dfs(chon1)
print(visited[chon2])
