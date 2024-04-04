# 풀이1) 순열 permutations 이용
from itertools import permutations # 순열
N, M = map(int, input().split())
arr = list(range(1, N+1))
for i in permutations(arr, M):
  print(*i,end='\n')

# 풀이2) 백트래킹
def dfs():
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()
N, M = map(int,input().split())
arr = []
dfs()
