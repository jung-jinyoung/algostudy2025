"""
N * M
바이러스는 상하좌우로 퍼짐
새로 세울 수 있는 벽의 개수는 3개, 꼭 3개를 세워야 함

안전 영역 크기의 최댓값을 구하라
"""
import copy
import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

# 0인 곳중 3곳을 고르는 조합
empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

# 바이러스 위치
virus_spots = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

# 바이러스 퍼트리기
def spread_virus(copy_lab):
    # 큐에 바이러스 위치 넣기
    queue = deque(virus_spots)
    # 상하좌우로 퍼짐
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and copy_lab[nx][ny] == 0:
                copy_lab[nx][ny] = 2
                queue.append((nx, ny))


# 벽을 세울 수 있는 모든 조합
max_safe = 0
for walls in combinations(empty_spaces, 3):
    copy_lab = copy.deepcopy(lab)

    # 벽 세우기
    for x, y in walls:
        copy_lab[x][y] = 1

    # 바이러스 확산
    spread_virus(copy_lab)

    # 안전영역 카운팅
    safe = sum(row.count(0) for row in copy_lab)
    max_safe = max(safe, max_safe)

print(max_safe)