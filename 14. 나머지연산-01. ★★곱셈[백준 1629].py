'''
지수법칙 : a^(n+m) = a^n * a^m
모듈러 성질 : (a*b)%c = (a%c * b%c)%c
재귀 함수로 지수 B를 절반으로 계속 나눠서

k = f(y/2)

짝수일 때 : k*k
홀수일 때 : k*k*A 로 지수법칙을 사용하여 시간복잡도를 O(log n)수준으로 낮춰주었다.
'''
A, B, C = map(int, input().split())
def solve(A, B):
    if B == 1: # 종료 조건
        return A % C

    k = solve(A, B // 2)

    if B % 2 == 0: #짝수일때 
        return (k * k)% C
    else:   #홀수일때
        return (k * k) * A % C
    
print(solve(A, B))
