#10818 결과:	153832kb,	388ms
import sys
n=int(sys.stdin.readline().rstrip())
numList = list(map(int, sys.stdin.readline().rstrip().split()))
print(min(numList), max(numList))
