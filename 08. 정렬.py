#선택정렬: 맨앞 숫자 이외에 나머지 숫자들 중 최솟값 찾아서 맨앞 숫자랑 자리바꿈
s=list(map(int, input().split()))
for i in range(len(s)):
	min_index=i
	for j in range(i+1, len(s)):
		if s[j]<s[min_index]: min_index=j #가장 작은 수 찾기
	s[i], s[min_index] = s[min_index], s[i] #작은수와 위치 변경
print(*s)

#버블정렬: 두개씩 비교해서 큰수 맨뒤에 고정
s=list(map(int, input().split()))
for i in range(len(s)):
	for j in range(len(s)-i-1): #큰수셋팅할 뒷자리 빼고까지 비교
		if s[j+1]<s[j]: 
			s[j], s[j+1] = s[j+1], s[j]
print(*s)

#삽입정렬
s=list(map(int, input().split()))
new=[s[0]]
for i in range(1, len(s)):
	j=0
	while j<i and new[j]<s[i]:
		j += 1
	new.insert(j, s[i])
print(*new)
