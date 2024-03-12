# 리스트 이용	31120kb	48ms
import sys
N=int(sys.stdin.readline().rstrip())
stack=[]
for _ in range(N):
    s=sys.stdin.readline().rstrip().split()
    if(s[0]=='push'): stack.append(s[1])
    elif(s[0]=='pop'): print(-1 if len(stack)==0 else stack.pop())
    elif(s[0]=='size'): print(len(stack))
    elif(s[0]=='empty'): print( 1 if len(stack)==0 else 0)
    elif(s[0]=='top'): print(-1 if len(stack)==0 else stack[len(stack)-1])
    
# deque 이용	34036kb	80ms
import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
dq=deque()
for _ in range(N):
    s=sys.stdin.readline().rstrip().split()
    if(s[0]=='push'): dq.append(s[1])
    elif(s[0]=='pop'): print(-1 if len(dq)==0 else dq.pop())
    elif(s[0]=='size'): print(len(dq))
    elif(s[0]=='empty'): print( 1 if len(dq)==0 else 0)
    elif(s[0]=='top'): print(-1 if len(dq)==0 else dq[len(dq)-1])    
