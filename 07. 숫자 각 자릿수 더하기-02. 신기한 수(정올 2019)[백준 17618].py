#100점, PyPy3 111592kb	2656ms
import sys
n=int(sys.stdin.readline().rstrip())
cnt=0
for i in range(1, n+1):
    tmp=sum([int(c) for c in str(i)])
    if i % tmp == 0: cnt+=1
print(cnt)

#78점, Python3 	31120kb	496ms
N = int(input())

def solve(n):
    si = str(n)
    tmp = 0
    for s in si:
        tmp += int(s)
    if n % tmp == 0:
        return True
    return False

ans = 0
for i in range(1, N+1):
    if solve(i):
        ans += 1

print(ans)
