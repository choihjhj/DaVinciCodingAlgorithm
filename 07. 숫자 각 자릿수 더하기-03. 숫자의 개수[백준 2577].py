#Python3 31252kb 44ms
A=int(input())
B=int(input())
C=int(input())
cnt=[0]*10
for i in str(A*B*C):
	cnt[int(i)]+=1
for i in cnt:
	print(i)	
