'''
최소힙(오름차순)
import heapq
heapq.heappush(리스트,데이터값)
heapq.pop(리스트)

최대힙(내림차순)
heapq.heappush(리스트,-데이터값)
-heapq.pop(리스트)
'''
#최대힙 이용(내림차순)
import heapq
import sys
N=int(sys.stdin.readline().rstrip())
heap=[]
for _ in range(N):
    x=int(sys.stdin.readline().rstrip())
    if x: heapq.heappush(heap, -x)
    else: 
        if len(heap):
            print(-heapq.heappop(heap))
        else: print(0)
