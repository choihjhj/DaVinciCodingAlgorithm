N = int(input())

cnt = 1
ans = 1 #껍질수 결과
while cnt < N:
    cnt += 6 * ans
    ans += 1

print(ans)
