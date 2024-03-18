import sys
input = sys.stdin.readline
n = int(input().rstrip())
s = []
for _ in range(n):
	s.append(tuple(map(int, input().rstrip().split())))
s.sort(ke y= lambda x: (x[1],x[0])) #내림차순 정렬
cnt = 0
maxx = -1
for i in s:
	if maxx <= i[0]:
		maxx = i[1]
		cnt += 1
print(cnt)
