import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=int(input().rstrip())
arr = [[] for _ in range(N+1)]
for i in range(1,N+1):
  v=int(input().rstrip())
  arr[i].append(v)

ans = []
def dfs(start, n):
    visited[n] = True
    for nn in arr[n]:
        if not visited[nn]: 
            dfs(start, nn)
        elif start == nn:
          ans.append(start)
          return

for i in range(1, N+1):
  visited = [False] * (N+1)
  dfs(i, i)

print(len(ans), *sorted(ans),sep='\n')
