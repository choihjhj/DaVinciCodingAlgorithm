# 코테 공부방법
1. 위키독스 점프투파이썬으로 파이썬 문법 공부 (https://wikidocs.net/book/7601)
2. 위키독스 다빈치 코딩 알고리즘으로 알고리즘 공부 (https://wikidocs.net/book/10280)
    

## [시간 단축 방법]
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
4) 변경 값이 없으면 list 대신 튜플사용
```
```
