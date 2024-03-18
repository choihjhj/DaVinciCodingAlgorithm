S, P = map(int, input().split())
dna = input()
max_dna = list(map(int, input().split()))

chk_dna = ('A', 'C', 'G', 'T')
cnt_dna = [0] * 4

def add_dna(d):
    for i in range(4):
        if d == chk_dna[i]:
            cnt_dna[i] += 1

def del_dna(d):
    for i in range(4):
        if d == chk_dna[i]:
            cnt_dna[i] -= 1

def check_dna():
    for i in range(4):
        if cnt_dna[i] < max_dna[i]:
            return False
    return True 

for d in dna[:P]:
    add_dna(d)

cnt = 1 if check_dna() else 0

for i in range(P, S):
    add_dna(dna[i])
    del_dna(dna[i - P])

    if check_dna():
        cnt += 1

print(cnt)
