A, B = map(int, input().split())
q = A // B
r = A % B
if r < 0: #음수인경우
    q += 1
    r -= B
print(q, r, sep='\n', end='')
