'''
모르겠음.....정올문제
'''
N = int(input())
honeys = [0] + list(map(int, input().split()))
hs = []
total = 0
for honey in honeys:
    total += honey
    hs.append(total)

def eat(i, j, k):
    # 1. i가 꿀
    sum_i1 = hs[j-1] - hs[i-1] # sum(honeys[i:j])
    sum_i2 = hs[k-1] - hs[i-1] - honeys[j] #sum(honeys[i:k]) - honeys[j]
    rst1 = sum_i1 + sum_i2

    # 2. j가 꿀
    sum_j1 = hs[j] - hs[i] # sum(honeys[i+1:j+1])
    sum_j2 = hs[k-1] - hs[j-1] # sum(honeys[j:k])
    rst2 = sum_j1 + sum_j2

    # 3. k가 꿀
    sum_k1 = hs[k] - hs[i] - honeys[j] # sum(honeys[i+1:k+1]) - honeys[j]
    sum_k2 = hs[k] - hs[j] # sum(honeys[j+1:k+1])
    rst3 = sum_k1 + sum_k2

    return max(rst1, rst2, rst3)

rst = 0
for j in range(2, N):
    temp = eat(1, j, N)
    rst = max(rst, temp)
print(rst)
