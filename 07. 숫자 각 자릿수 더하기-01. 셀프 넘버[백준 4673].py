A = set(range(1, 10000))
B = set()  #중복생성자 없도록 하기위해서
for x in A :
    for y in str(x):
        x += int(y)
    B.add(x)  
C = A - B  
for x in sorted(C):  
    print(x)
