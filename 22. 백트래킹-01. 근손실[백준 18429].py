'''브루트포스 알고리즘 + 백트래킹 문제'''
풀이1) 순열 permutations 이용
from itertools import permutations
import sys
input=sys.stdin.readline
N,K=map(int, input().split())
arr=list(map(int, input().split()))
cnt=0
for i in permutations(arr,N):
    w=500
    for j in i:
        w+=j-K
        if w<500: break
    if w>=500: cnt+=1            
print(cnt)

풀이2) 백트래킹
import sys
input=sys.stdin.readline
N, K = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
ans = 0
visited = [False] * N
def dfs(n, weight):
    global ans
    if weight < 500:
        return
    if n == N:
        ans += 1
        return
    weight -= K
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n + 1, weight + A[i])
            visited[i] = False
dfs(0, 500)
print(ans)
