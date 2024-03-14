# 풀이1)
N=int(input())
a=list(range(1,N+1))
while len(a)!=1:
    a=a[1::2]
print(a[0])


# 풀이2)
N = int(input())
ans = 1
while ans * 2 <= N:
    ans *= 2
print(ans)
