# 풀이1) 이코테 방법
import sys
n=int(sys.stdin.readline()) #15
sum,end,cnt=0,0,0
for start in range(1,n+1):
    while end<=n and sum<n:
        sum+=end
        end+=1
    if sum==n:
        cnt+=1
    sum-=start
print(cnt) #4   

# 풀이2) 다빈치코딩알고리즘 풀이
n=int(input())
arr=range(1,n+1)
summ=0
s,e=0,0
result=0
while True:
  if n<=summ:
    summ-=arr[s]
    s+=1
  else:
    if e==n: break
    summ+=arr[e]
    e+=1

  if summ==n:
    result+=1
print(result)
