from collections import deque

N = int(input())
for _ in range(N):
    w, h = map(int, input().split())
    arr = list(list(input()) for _ in range(h))   #'.': 빈 공간, '#': 벽, '@': 상근이의 시작 위치, '*': 불
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    q = deque()
    q.append(deque())
    q.append(deque())   # 0번째는 상근이의 다음위치 1번째는 불의 다음위치
    for a in range(h):
        for b in range(w):
            if arr[a][b] == '@':
                q[0].append((a, b))
            elif arr[a][b] == '*':
                q[1].append((a, b))
    def bfs():
        cnt = 0
        while True:
            if not q[0]:
                return "IMPOSSIBLE"

            human = deque()
            fire = deque()  # 현재 불의 위치
            while q[1]:
                fi, fj = q[1].popleft()
                for z in range(4):
                    ffi = fi + di[z]
                    ffj = fj + dj[z]
                    if (0 <= ffi < h) and (0 <= ffj < w) and (arr[ffi][ffj] not in "*#"):
                        fire.append((ffi, ffj))
                        arr[ffi][ffj] = "*"
            q[1] = fire
            while q[0]:
                ni, nj = q[0].popleft()
                for y in range(4):
                    nni = ni + di[y]
                    nnj = nj + dj[y]
                    if (0 <= nni < h) and (0 <= nnj < w) and (arr[nni][nnj] not in "#@*"):
                        human.append((nni, nnj))
                        arr[nni][nnj] = "@"
                cnt += 1
            q[0] = human
    print(bfs())