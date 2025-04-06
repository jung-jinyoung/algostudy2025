from collections import deque

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
mh = max(max(area) for area in arr)
def dfs(x, y, h):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    q = deque()
    q.append((x, y))
    while q:
        nx, ny = q.pop()
        visited.add((nx, ny))
        for b in range(4):
            ni = nx + di[b]
            nj = ny + dj[b]
            if (0 <= ni < N) and (0 <= nj < N) and ((ni, nj) not in visited) and (arr[ni][nj] > h):
                q.append((ni, nj))

res = 0
for a in range(mh):
    visited = set()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (arr[i][j] > a) and ((i, j) not in visited):
                cnt += 1
                dfs(i, j, a)
    res = max(res, cnt)
print(res)