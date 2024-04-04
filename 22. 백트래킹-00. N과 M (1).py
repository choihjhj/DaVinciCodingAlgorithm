# 풀이1) 순열 permutations 이용
from itertools import permutations # 순열
N, M = map(int, input().split())
arr = list(range(1, N+1))
for i in permutations(arr, M):
  print(*i,end='\n')
