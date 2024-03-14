N = int(input())
arr = [int(input()) for _ in range(N)]
cnt = 0
max_a = 0
for a in reversed(arr):
    if max_a < a:
        cnt += 1
        max_a = a
print(cnt)


# n=int(input())
# arr=[int(input()) for _ in range(n)]
# tmp=arr[len(arr)-1]
# arr.sort(reverse=True)
# idx=arr.find(tmp)
# print(len(arr[:idx+1]))
