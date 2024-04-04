# 풀이1) 백트래킹
'''
1.아이디어
- 백트래킹 재귀함수 안에서, for문 돌면서 숫자 선택(이때 방문여부 체크)
- 재귀함수에서 M개를 선택할 경우 print 후 return
2. 시간복잡도
- (1 ≤ M ≤ N ≤ 8)이고, 중복불가니까 O(N!)로 백트래킹 가능
3. 자료구조
- 결과값 저장 int[]
- 방문여부체크 bool[]
'''
import sys
input=sys.stdin.readline
N, M=map(int,input().split())
arr=[]
visited=[False]*(N+1)
def backtraking(num):
    if num==M:
        print(*arr)
        return
    for i in range(1,N+1): #부모탐색
        if not visited[i]:
            visited[i]=True
            arr.append(i)
            backtraking(num+1) #자식탐색
            visited[i]=False
            arr.pop()
backtraking(0)

# 풀이2) 순열 permutations 이용
from itertools import permutations # 순열
N, M = map(int, input().split())
arr = list(range(1, N+1))
for i in permutations(arr, M):
  print(*i)

''' 참고링크: https://youtu.be/atTzqxbt4DM?si=Qgufvn-_GyU6oA52 '''
