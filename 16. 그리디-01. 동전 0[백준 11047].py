import sys
n,k=map(int, sys.stdin.readline().rstrip().split())
coin=[int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt=0
for c in coin[::-1]:
    cnt += k//c
    k %= c
print(cnt)
'''
동전 문제는 추 후 DP를 배우고 나면 다른 방식으로 풀어보겠습니다. 배수가 아닌 상황에서는 그리디로 풀 수 없기 때문에 다른 방식으로 풀어주어야 합니다.
'''
