import sys
input=sys.stdin.readline
N,M=map(int, input().rstrip().split())
d=[int(i) for i in range(N+1)]
for _ in range(M):
    i,j=map(int, input().rstrip().split())
    d[i], d[j] = d[j], d[i]
print(*d[1:])
