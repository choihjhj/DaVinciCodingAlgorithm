# 풀이1)
'''
공 6개 : 1, 2, 3 - 두 값의 차 2 # N % K 나누어떨어지면 바구니-1이 큰수작은수 차이임
공 7개 : 1, 2, 4 - 두 값의 차 3 # N % K 나머지가 있으면 바구니수가 큰수작은수 차이임
공 8개 : 1, 3, 4 - 두 값의 차 3
공 9개 : 2, 3, 4 - 두 값의 차 2
공 10개 : 2, 3, 5 - 두 값의 차 3
'''
N, K = map(int, input().split())
N -= (K+1) * K // 2 # N-=sum(range(1,K+1)) 같은결과임, 등차수열합

if N < 0: 
    print(-1)
else:
    if N % K: #나머지가 있으면 바구니수가 큰수작은수 차이임
        print(K)
    else: #나누어떨어지면 바구니-1이 큰수작은수 차이임
        print(K-1)
# 풀이2)
N, K = map(int, input().split())
summ = (K+1) * K // 2 #등차수열합

if N < summ:
    print(-1)
else:
    N-=summ
    if N % K:
        print(K)
    else:
        print(K-1)
