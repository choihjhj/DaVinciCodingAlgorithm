# 풀이1) 순열 permutations 이용
from itertools import permutations # 순열
N, M = map(int, input().split())
arr = list(range(1, N+1))
for i in permutations(arr, M):
  print(*i,end='\n')

# 풀이2) 백트래킹
import sys
input=sys.stdin.readline
N, M=map(int,input().split())
arr=[]
visited=[False]*(N+1)
def backtraking(num):
    if num==M:
        print(*arr)
        return
    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            arr.append(i)
            backtraking(num+1)
            visited[i]=False
            arr.pop()
backtraking(0)
