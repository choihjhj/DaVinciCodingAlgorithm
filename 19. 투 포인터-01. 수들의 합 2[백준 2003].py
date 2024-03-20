# 풀이1) 다빈치 코딩 알고리즘 풀이
N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
sum_arr = 0
ans = 0
while True:
    if M <= sum_arr:
        sum_arr -= arr[start]
        start += 1
    else:
        if end == N:
            break
        sum_arr += arr[end]
        end += 1

    if sum_arr == M:
        ans += 1
print(ans)

# 풀이2) 이코테 책풀이
n,m=map(int, input().split())
arr=list(map(int, input().split()))
e,cnt,summ=0,0,0
for s in range(n):  #s를 차례대로 증가시키며 반복
  while e<n and summ<m: #e를 가능한 만큼 이동시키
    summ+=arr[e]
    e+=1
  if summ==m: #부분합이 m일 때 카운트 증
    cnt+=1
  summ-=arr[s]
print(cnt)
