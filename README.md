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
3) sort 우선순위
```
```
