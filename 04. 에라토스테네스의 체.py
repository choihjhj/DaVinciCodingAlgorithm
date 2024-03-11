n=5
prime=[True]*(n+1)
prime[0], prime[1]= False, False #0과 1은 소수가 아니므로 False
for i in range(2, int(n**0.5) + 1): # 2부터 제곱근까지만 반복
    if prime[i]: # prime[i]가 True이면 소수입니다.
        for j in range(i * 2, n+1, i): # i * 2부터 i의 배수를 순회합니다.
            prime[j] = False # i의 배수는 모두 소수가 아닙니다.
print(f'2부터 {n} 까지 소수는 총 {prime[2:n+1].count(True)}개 있습니다.')           
 
# result = 0
# for i in range(2,n+1):
#     if prime[i]:
#         result += 1
# print(f'2부터 {n} 까지 소수는 총 {result}개 있습니다.')
