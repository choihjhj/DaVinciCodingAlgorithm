import sys
n,k=map(int, sys.stdin.readline().rstrip().split())
coin=[int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt=0
for c in coin[::-1]:
    cnt += k//c
    k %= c
print(cnt)
'''
동전이 서로 배수인 경우엔 그리디 알고리즘으로 문제풀이 한다.
배수가 아닌 상황에서는 그리디가 아닌 DP 방법으로 풀어주어야 한다.
'''
