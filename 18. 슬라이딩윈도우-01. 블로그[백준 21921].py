N, X = map(int, input().split())
arr = list(map(int, input().split()))
sw = sum(arr[:X])
max_sum = sw
cnt = 1
for i in range(X, N):
    sw = sw - arr[i - X] + arr[i]
    if sw == max_sum: #최대합 같은거 발견하면 cnt 1증가
        cnt += 1
    elif max_sum < sw: #더 큰거 발견하면 max값 바꾸고 cnt=1로 셋팅
        max_sum = sw
        cnt = 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(cnt)
