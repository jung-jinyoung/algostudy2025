"""
안전구역의 min과 max를 뽑아서 범위 설정

각 강수량 마다 visited 배열을 생성해서 방문하지 않은 곳 있으면
좌표를 bfs 함수에 보내기

bfs 함수에서 deque로 좌표를 받고 상하좌우를 탐색.
탐색 종료시 cnt += 1

그렇게 모든 맵에서 완료하면 cnt랑 max_cnt랑 비교.
"""

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
max_safe = 0

"""
max_height = max(max(city))
min_height = min(min(city))
때문에 계속 틀렸었음.
파이썬은 리스트를 사전순으로 비교하기 때문
"""

max_height = max(map(max, city))
min_height = min(map(min, city))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x, i, visited):
    # 갈 수 있는 곳의 좌표를 visit_location에 담아서 return
    visit_location = deque()
    visit_location.append((y, x))
    visited[y][x] = 1
    while visit_location:
        y, x = visit_location.popleft()

        for g in range(4):
            ny = dy[g] + y
            nx = dx[g] + x

            if 0 <= nx < n and 0 <= ny < n and city[ny][nx] > i and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                visit_location.append((ny, nx))


for i in range(min_height - 1, max_height + 1):
    visited = [([0] * n) for _ in range(n)]
    safe = 0
    for k in range(n):
        for l in range(n):
            # 시작점 발견시
            if city[k][l] > i and visited[k][l] == 0:
                bfs(k, l, i, visited)
                safe += 1
    if safe > max_safe:
        max_safe = safe

print(max_safe)