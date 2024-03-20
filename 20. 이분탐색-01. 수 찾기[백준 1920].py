#풀이1) 그냥풀기 :시간초과 나옴, 제한시간 1초인데 (1 ≤ N,M ≤ 100,000)이니까 in의 시간복잡도는 O(n)이므로 for문이랑 합쳐진 O(n^2) 10,000,000,000으로 1초(100,000,000) 넘음
import sys
n=int(sys.stdin.readline()) 
A=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline()) 
B=list(map(int, sys.stdin.readline().rstrip().split()))
for i in B:
    print(1 if i in A else 0)

#풀이2) from bisect import bisect_left 이용, for문 O(M)에 bisect_left O(logN)사용했으므로 O(MlogN), 48764kb	252ms 아래 이분탐색 직접 구현보다 더 빠름
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
    
#풀이3) 이진탐색으로 풀기, 이것도 O(MlogN), 	48780kb	436ms
import sys
from bisect import bisect_left
n=int(sys.stdin.readline()) 
A=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline()) 
B=list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
def binary_search(k):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == k:
            return 1
        if A[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return 0
for q in B:
    print(binary_search(q))

