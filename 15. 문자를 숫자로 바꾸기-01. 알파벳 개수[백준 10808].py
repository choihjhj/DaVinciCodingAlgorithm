s=input()
cnt=[0]*26
for c in s:
    cnt[ord(c)-ord('a')] +=1
print(*cnt)
