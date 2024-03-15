# 풀이1) 	31120kb	72ms 
n=int(input())
a=[]
for _ in range(n):
    A,B=map(int, input().split())
    if A<=B: a.append(B)
print(min(a) if a else -1)

# 풀이2) 	31120kb	48ms
N = int(input())
MAX = 10000
result = MAX
for _ in range(N):
    arrival_time, open_time = map(int, input().split())
    if open_time < arrival_time:
        continue
    if open_time < result:
        result = open_time
if result == MAX:
    print(-1)
else:
    print(result)
