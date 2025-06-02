from collections import deque
def solution(land):
    y, x = len(land), len(land[0])
    num = 10
    ans = 0
    data = []
    for i in range(y):
        for j in range(x):
            if land[i][j] == 1:
                cnt = 1
                q = deque()
                q.append((i, j))
                land[i][j] = num
                while q:
                    iii, jjj = q.popleft()
                    for ni, nj in ((iii, jjj - 1), (iii, jjj + 1), (iii + 1, jjj), (iii - 1, jjj)):
                        if 0 <= ni < y and 0 <= nj < x and land[ni][nj] == 1:
                            land[ni][nj] = num
                            cnt += 1
                            q.append((ni, nj))
                data.append(cnt)
                num += 1
    for i in range(x):
        cnt = 0
        arr = set()
        for j in range(y):
            if land[j][i]:
                arr.add(land[j][i] - 10)

        for nnn in list(arr):
            cnt += data[nnn]
        ans = max(ans, cnt)
    return ans