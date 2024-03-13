import sys
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
	stack=[]
	check = False
	s=sys.stdin.readline().rstrip()
	for c in s:
		if c=='(': stack.append(c)
		elif c==')':
			if not stack: #비어있는데 pop못하니까 break후 바로 NO로 가기
				check = True
				break 
			stack.pop()
	print( "NO" if stack or check else "YES")
