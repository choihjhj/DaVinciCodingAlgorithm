from collections import deque
M, N = map(int, input().split())
arr = []
queue = deque()
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 1:
            queue.append((i, j))

d = d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
def bfs():  
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
bfs()
def get_day():
    ans = 0
    for row in arr:
        if 0 in row:
            return -1

        row_max = max(row)    
        if ans < row_max:
            ans = row_max
    return ans - 1
print(get_day())
