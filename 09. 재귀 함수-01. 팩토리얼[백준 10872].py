N = int(input())

def fac(n):
    # 0이되면 1리턴
    if n <= 1: return 1
    return n * fac(n-1)

print(fac(N))
