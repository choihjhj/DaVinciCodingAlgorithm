import sys
input=sys.stdin.readline
N, K= map(int, input().rstrip().split()) #5 3
arr=list(map(int,input().rstrip().split() )) #5 4 3 2 1
summ=[0]*(N+1)
summ[1]=arr[0]
for i in range(1,N): #0 5 9 12 14 15
    summ[i+1]=summ[i]+arr[i]

for _ in range(K):    
    i,j=map(int, input().rstrip().split())
    print(summ[j]-summ[i-1])
