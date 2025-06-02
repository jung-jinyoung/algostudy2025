import sys

input = sys.stdin.readline

# sys.stdin = open('input.txt', 'r')

"""
이진탐색으로 풀자
python3는 시간초과
pypy3는 통과 / 메모리 258500KB / 시간 452ms

"""
n, m = map(int, input().split())
trees_high = list(map(int, input().split()))

answer = 0

left = 0
right = max(trees_high)

while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in range(n):
        if trees_high[i] > mid:
            total += trees_high[i] - mid
    # total이 m이상일 경우 일단 저장 후 왼쪽 조정
    if total >= m:
        left = mid + 1
        answer = mid
    # 높이가 너무 높아서 total이 m 보다 작을 경우
    else:
        right = mid - 1

print(answer)