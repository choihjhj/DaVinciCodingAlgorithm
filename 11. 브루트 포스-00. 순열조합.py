브루트 포스(Brute Force)는 알고리즘이라기 보다는 모든 경우를 다 따지며 해를 찾는 방식
문제를 어떻게 풀어야 할지 모를 때 브루트 포스로 문제를 풀다보면 해결할 방법이 보일 수도 있고, 부분점수라도 얻을 수 있기 때문에 꼭 알아두어야 함

조합(Combination)-순서없음
from itertools import combinations
list(combinations(리스트, 조합수))
조합 개수 nCr= n*...*(n-r-1)/(r*..*1)
10C3=10 * 9 * 8 / (3 * 2 * 1)

순열(Permutation)-순서있음, 모든 경우의 수
from itertools import permutations
list(permutations(리스트, 순열수))
순열 개수 nPr = n*...*(n-r-1)
10P3=10*9*8

