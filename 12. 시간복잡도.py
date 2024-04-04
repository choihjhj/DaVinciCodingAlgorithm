시간복잡도 빅오표기법
O(1) < O(logN) < O(N) < O(NlogN) < O(N^2) < O(N^3) < O(2^n) < O(n!)
O(N/2)이 O(logN)라고 보면 됨
  
시간제한이 1초인 문제를 만났을 떄, (1초는 100,000,000임, 1억)
N의 범위가 500인 경우: 시간복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 출 수 있다.
N의 범위가 2,000인 경우: 시간복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 출 수 있다.
N의 범위가 100,000인 경우: 시간복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 출 수 있다.
N의 범위가 10,000,000인 경우: 시간복잡도가 O(N)인 알고리즘을 설계하면 문제를 출 수 있다.

log2000000는 5.xx임 그래서 O(NlogN)인 알고리즘 적절
시간초과 됐을 때 PyPy로 제출해 보거나, Python으로 제출하기
보통 시간제한 1~5초 라고 생각하기

O(1)
리스트에서 인덱스를 사용하여 데이터 찾을 때
- 변수명.append()
사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회한다.
O(logN)
이진 트리 탐색, 우선순위큐PriorityQueue()힙정렬
O(N)
정렬되지 않은 배열에서 데이터 검색 등
투포인터(부분합)
- 변수명.reverse()
- 변수명.insert(인덱스,특정값)
- 변수명.count(특정값)
- 변수명.remove(특정값) #특정값이 여러개면 하나만 지움
O(NlogN)
퀵정렬, 머지정렬 등 ,heappush랑 heappop은 O(nlogn) 우선순위큐의 put,get도
- 변수명.sort()
- 변수명.sort(reverse=True) #내림차순 정렬

O(N^2)
버블 정렬, 삽입정렬 등
O(N^3)
편상관관계 계산 등
O(2^n)
피보나치, Brutal Force 등
O(n!)
완전탐색(Brutal Force)무작위 대입     
순열, 조합   
중복없는 백트래킹    

# 순열-서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
{'A','B','C'}에서 3개를 선택하여 나열하는 경우:'ABC','ACB','BAC','BCA','CAB','CBA'
from itertools import permutations
data=['A','B','C']
result=list(permutations(data,3)) #3개 뽑아 3P3 모든 순열 구하기
print(result) 
#[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합-서로 다른 n개에서 순서 상관 없이 서로 다른 r개를 선택하는 것
from itertools import combinations
data=['A','B','C']
result=list(combinations(data,2)) #2개 뽑아 3C2 모든 조합 구하기
print(result) #[('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열
from itertools import product
data=['A','B','C']
result=list(product(data,repeat=2)) #2개를 뽑는 모든 순열 구하기(중복 허용)

# 중복 조합
from itertools import combinations_with_replacement
data=['A','B','C']
result=list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기(중복 허용)

코테풀 때
1. 1초에 1천만번 연산
2. 데이터개수(N)를 보고 적절한 시간복잡도의 알고리즘 떠올리기
3. 종이에 알고리즘 정하고 코딩하기
