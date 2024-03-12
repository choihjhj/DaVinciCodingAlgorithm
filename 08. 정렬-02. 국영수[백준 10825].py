import sys
N = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(N):
    name, *scores = sys.stdin.readline().rstrip().split()
    arr.append((name, *map(int, scores)))

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for st in arr:
    print(st[0])
