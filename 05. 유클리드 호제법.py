# 방법1) 재귀
a, b = map(int, input().split())

def gcd(a, b):
    return b if a%b==0 else gcd(b,a%b)

print(gcd(a, b))

# 방법2) math.gcd 함수 이용
import math
a, b = map(int, input().split())
print(math.gcd(a,b)) 

# 방법3) while문
a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a 

print(gcd(a, b))
