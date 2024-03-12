N = int(input())

arr = []
for _ in range(N):
    name, *scores = input().split()
    arr.append((name, *map(int, scores)))

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0])) #우선순위 -내림차순, +오름차순

for st in arr:
    print(st[0])
