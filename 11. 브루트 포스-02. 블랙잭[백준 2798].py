from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
my_max = 0
for select_card in combinations(arr, 3):
    my_sum = sum(select_card)
    if my_max < my_sum <= M:
        my_max = my_sum
print(my_max)  
