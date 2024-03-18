'''
2차원 배열이라 까다로운 문제임
합 구할 때 dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i][j] 이렇게 해야 하고
출력힐 때도 dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
참고링크) https://youtu.be/irLF8gaAoGk?si=YB39OB5nWJq_gBBD
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]*(n+1)]
for i in range(n):
    arr.append([0]+list(map(int, input().split())))
    
dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i][j]
        
for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())    
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)
