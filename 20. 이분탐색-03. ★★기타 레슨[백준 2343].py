N, M = map(int, input().split())
disc = list(map(int, input().split()))
left, right = max(disc), sum(disc)
while left <= right:
    mid = (left + right) // 2
    cnt, total = 1, 0
    for d in disc:
        if total + d <= mid:
            total += d
        else:
            total = d
            cnt += 1

    if M < cnt:
        left = mid + 1
    else:
        right = mid - 1
print(left)
