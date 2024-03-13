import sys
input=sys.stdin.readline
k=int(input())
s=[]
for _ in range(k):
    num=int(input())
    if num: 
        s.append(num)
    else:
        s.pop()
print(sum(s)) 
