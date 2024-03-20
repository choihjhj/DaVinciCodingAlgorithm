# 풀이1) 이분탐색 bisect 모듈 이용 , PyPy3 274784kb	1176ms	
from bisect import bisect_left
N=int(input())
a=list(map(int, input().split()))
b=sorted(list(set(a)))
for i in a:
    idx=bisect_left(b,i)
    print(idx,end=' ')

# 풀이2) dict 이용, 308100kb	1152ms
from bisect import bisect_left
N=int(input())
a=list(map(int, input().split()))
b={x:i for i, x in enumerate(sorted(list(set(a))))}
for i in a:
    print(b[i],end=' ')
