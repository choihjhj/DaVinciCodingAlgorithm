'''유튜브 바킹독에서 추천한 문제
'''
#풀이1) bisect 모듈 이용
from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

def binary_search(b):
    bl = bisect_left(A, b)
    if bl < len(A) and A[bl] == b:
        br = bisect_right(A, b)
        return br - bl
    else:
        return 0

for b in B:
    print(binary_search(b), end=' ')

#풀이2) Counter 모듈 이용
from collections import Counter

N = int(input())
cards = Counter(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

result = []
for target in targets:
    result.append(cards[target])

print(*result)
