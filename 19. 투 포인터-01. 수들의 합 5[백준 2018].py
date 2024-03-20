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
