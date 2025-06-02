from collections import deque
T = int(input())
for tc in range(T):
    brk_point = 0
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]

    q = deque()  # 0: 불, 1 이상: 상근이 이동 수
    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                q.append((0, i, j))  # 불 먼저
            elif arr[i][j] == '@':
                arr[i][j] = '.'
                si, sj = i, j

    q.append((1, si, sj))  # 상근 나중
    visited[si][sj] = True

    while q:
        idx, i, j = q.popleft()
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= ni < h and 0 <= nj < w:
                if idx == 0:  # 불
                    if arr[ni][nj] == '.':
                        arr[ni][nj] = '*'
                        q.append((0, ni, nj))
                else:  # 상근
                    if arr[ni][nj] == '.' and visited[ni][nj]==0:
                        visited[ni][nj] = 1
                        q.append((idx + 1, ni, nj))
            else:
                if idx:  # 상근이 탈출
                    print(idx)
                    brk_point = 1
                    break
        if brk_point:
            break
    else:
        print('IMPOSSIBLE')