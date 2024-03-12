'''
셀프넘버가 아닌 수는 자기자신+각자릿수의합
'''
A = set(range(1, 10000))
B = set()  #중복생성자 없도록 하기위해서
for x in A :
    for y in str(x):
        x += int(y)
    B.add(x)  #셀프넘버 아닌 수
C = A - B  #셀프넘버
for x in sorted(C):  
    print(x)
