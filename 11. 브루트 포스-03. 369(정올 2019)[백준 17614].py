#풀이1) 	110272kb	180ms
N=int(input())
cnt=0
for i in range(1,N+1):
    str_num = str(i)
    for c in '369':
        cnt += str_num.count(c)
print(cnt)

#풀이2) 	110272kb	208ms
N=int(input())
cnt=0
for i in range(1,N+1):
    for c in str(i):
        if c in '369': cnt+=1
print(cnt)
