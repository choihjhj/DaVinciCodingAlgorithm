'''브루트포스 알고리즘 + 백트래킹 문제'''
# 풀이1) 순열 permutations 이용
from itertools import permutations
import sys
input=sys.stdin.readline
N,K=map(int, input().split())
A = list(map(int, input().split()))
cnt=0
for i in permutations(A, N):
    w=500
    for j in i:
        w+=j-K
        if w<500: break
    if w>=500: cnt+=1            
print(cnt)

# 풀이2) 백트래킹1
import sys
input=sys.stdin.readline
N, K = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
cnt = 0
visited = [False] * N
def dfs(n, weight):
    global cnt
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if not visited[i] and weight+A[i]-K >= 500 :
            visited[i] = True
            dfs(n + 1, weight + A[i]-K)
            visited[i] = False
dfs(0, 500)
print(cnt)
