N, d, k, c = map(int, input().split())
arr=[int(input()) for _ in range(N)]
cnt=0

for i in range(N):
    eat_sushi = 1
    check = [0] * (d+1)
    check[c] = 1
    for j in range(i, i+k):
        sushi = arr[j % N]

        if not check[sushi]:
            eat_sushi += 1
        check[sushi] += 1
    cnt = max(cnt, eat_sushi)

print(cnt)
'''
백준 15961번: 회전 초밥
슬라이딩 윈도우 방법으로 푸는 문제
https://www.acmicpc.net/problem/15961
'''
