#풀이1) 이분탐색
import sys
K,N=map(int, sys.stdin.readline().rstrip().split())
cm=[int(sys.stdin.readline().rstrip()) for _ in range(K)]
start=1
end= max(cm)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in cm:
        cnt += line // mid

    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)

#풀이2) bisect 모듈 이용
import sys
from bisect import bisect_right

K,N=map(int, sys.stdin.readline().rstrip().split())
cm=[int(sys.stdin.readline().rstrip()) for _ in range(K)]
start=1
end= max(cm)
while start <= end:
    mid = (start + end) // 2
    cnt = sum(bisect_right(cm, mid*i) for i in range(1, N+1))
    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)
