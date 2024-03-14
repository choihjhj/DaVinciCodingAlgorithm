'''
막대기 문제는 역순으로 max값 발견했을 때 max 다시 셋팅 후 카운팅 하는게 핵심
즉, 1. 배열 역순 검사 2. 최댓값 업데이트가 핵심
'''
N = int(input())
arr = [int(input()) for _ in range(N)]
cnt=0
max_num=-1
for i in arr[::-1]:
    if max_num<i:
        cnt+=1
        max_num=i
print(max_num)
