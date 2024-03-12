'''
최소힙(오름차순)
import heapq
heapq.heappush(리스트,데이터값)
heapq.pop(리스트)

최대힙(내림차순)
heapq.heappush(리스트,-데이터값)
-heapq.pop(리스트)
'''
import heapq
import sys 

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    qst = int(input())

    if qst:
        heapq.heappush(heap, -qst)
    else:
        if len(heap):
            temp = heapq.heappop(heap)
            print(-temp)
        else:
            print(0)
