import sys
from heapq import heappush, heappop

input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    test = int(input())
    # 0 입력 = 가장 작은 값 출력 후 제거
    if (test == 0) :
        if (len(h) > 0):
            print(heappop(h))
        else:
            print(0)
        continue
    heappush(h, test)   