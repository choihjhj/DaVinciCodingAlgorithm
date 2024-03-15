import sys
n,k=map(int, sys.stdin.readline().rstrip().split())
coin=[int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt=0
for c in coin[::-1]:
    cnt += k//c
    k %= c
print(cnt)
