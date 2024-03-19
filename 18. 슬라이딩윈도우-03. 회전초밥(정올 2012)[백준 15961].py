N, d, k, c = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

check = [0] * (d+1)
check[c] = 1
eat_sushi = 1

for i in range(k):
    sushi = arr[i % N]

    if not check[sushi]:
        eat_sushi += 1

    check[sushi] += 1
max_sushi = eat_sushi

for i in range(N):
    start = arr[i % N]
    end = arr[(i + k) % N]

    check[start] -= 1
    if not check[start]:
        eat_sushi -= 1

    if not check[end]:
        eat_sushi += 1

    check[end] += 1
    max_sushi = max(max_sushi, eat_sushi)

print(max_sushi)
