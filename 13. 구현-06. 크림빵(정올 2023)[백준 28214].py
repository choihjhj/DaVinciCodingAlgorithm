n,k,p=map(int,input().split())
arr=input().split()
cnt=0
for i in range(0,n*k,k):
    if arr[i:i+k].count('0')<p: cnt+=1
print(cnt)
