N, K = map(int, input().split())
arr = list(map(int, input().split()))

sa = []
total = 0
for a in arr:
    total += a
    sa.append(total)

result = sa[K - 1]
for i in range(K, N):
    temp = sa[i] - sa[i - K]
    result = max(result, temp)
print(result)


# 슬라이딩 윈도우로 풀었을 때 코드
N, K = map(int, input().split())

arr = list(map(int, input().split()))
result = sum(arr[:K])

temp = result
for i in range(K, N):
    temp += arr[i] - arr[i-K]
    result = max(result, temp)

print(result)
