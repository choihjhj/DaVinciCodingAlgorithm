# 코테 공부방법   
1. 위키독스 점프투파이썬으로 파이썬 문법 공부 (https://wikidocs.net/book/7601)
2. 위키독스 다빈치 코딩 알고리즘으로 알고리즘 공부 1회독   (https://wikidocs.net/book/10280)
<!--3. 다빈치코딩알고리즘 2회독
4. 이코테 책 -->
<!-- 
3. 이코테 파이썬 책 공부 +  Do it! 알고리즘 코딩테스트(Python) 책공부
4. 백준 알고리즘 분류 제출순으로 풀기 (https://www.acmicpc.net/problem/tags)
-->    
# 시간복잡도 빅오표기법
## O(1) < O(logN) < O(N) < O(NlogN) < O(N^2) < O(N^3) < O(2^n) < O(n!)
**O(1)**     
리스트에서 인덱스를 사용하여 데이터 찾을 때    
- 변수명.append()
사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회한다.
          
**O(logN)**     
이진 트리 탐색, 우선순위큐PriorityQueue()힙정렬     
         
**O(N)**     
정렬되지 않은 배열에서 데이터 검색 등     
투포인터(부분합)     
- 변수명.reverse()
- 변수명.insert(인덱스,특정값)
- 변수명.count(특정값)
- 변수명.remove(특정값) #특정값이 여러개면 하나만 지움
        
**O(NlogN)**     
퀵정렬, 머지정렬 등 ,heappush랑 heappop은 O(nlogn) 우선순위큐의 put,get도     
- 변수명.sort()
- 변수명.sort(reverse=True) #내림차순 정렬
       
**O(N^2)**   
버블 정렬, 삽입정렬 등   
       
**O(N^3)**   
편상관관계 계산 등   
        
**O(2^n)**   
피보나치, Brutal Force 등   
         
**O(n!)**   
완전탐색(Brutal Force)무작위 대입     
중복, 순열, 백트래킹
   
---
### [시간 단축 방법]
1) 컴파일 에러시 재귀함수 깊이 제한 (Python3만 적용가능, PyPy3는 적용안됨)
```
import sys 
sys.setrecursionlimit(10**6)
```
2) 입력값 for문으로 많을 때
```
import sys
arr = map(int, sys.stdin.readline().rstrip().split())
```
3) sort 우선순위 조건 key=lambda x: x[0]으로 조건 추가
```
#-내림차순, +오름차순
arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0])) # 첫번째로 x[1] 내림차순 정렬, x[1]이 같으면 두번째로 x[2] 오름차순 정렬, x[1],x[2] 같으면 세번째로 x[3] 내림차순 정렬,x[1],x[2],x[3]이 같으면 네번째로 x[0] 오름차순 정렬 
```
4) 변경 값이 없으면 list([]) 대신 list((,))튜플사용
```
import sys
N = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(N):
    name, *scores = sys.stdin.readline().rstrip().split()
    arr.append((name, *map(int, scores)))

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0])) #-내림차순, +오름차순

for st in arr:
    print(st[0])
```
5) 메모리보다 속도가 중요하면 Python 대신 PyPy로 제출 
6) 이분탐색 O(logN) 사용할 때, from bisect import bisect_left, bisect_right 이용하기
```
import sys
from bisect import bisect_left
n=int(sys.stdin.readline()) 
A=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline()) 
B=list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
for i in B:
    idx=bisect_left(A,i)
    print(1 if idx<n and A[idx]==i else 0)
```
