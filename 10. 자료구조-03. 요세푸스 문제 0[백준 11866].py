#	34008kb	120ms
import sys
from collections import deque
N,K=map(int,sys.stdin.readline().rstrip().split())
dq=deque(range(1,N+1))
subdq=deque()
while dq:
    i=1
    while i<K:
        dq.append(dq.popleft())
        i+=1
    subdq.append(dq.popleft())    
print('<', end='')    
print(*subdq, sep=', ', end='')
print('>')
