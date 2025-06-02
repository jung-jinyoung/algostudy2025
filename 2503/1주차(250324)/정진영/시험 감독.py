import sys
import math

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for i in range(n):
    # 현재 시험장의 응시생 수
    a = arr[i]
    answer += 1 
    if (a-b >0):
        answer +=  math.ceil((a-b) / c)
print(answer)