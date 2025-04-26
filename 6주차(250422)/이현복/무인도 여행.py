from collections import deque
def solution(maps):
    answer = []
    n,m = len(maps),len(maps[0])
    v = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if v[i][j] == 0:
                v[i][j]^=1
                if maps[i][j] != 'X':
                    q = deque()
                    q.append((i,j))
                    cnt = int(maps[i][j])
                    while q:
                        I,J = q.popleft()
                        for ni,nj in ((I,J-1),(I,J+1),(I+1,J),(I-1,J)):
                            if 0<=ni<n and 0<=nj<m and v[ni][nj]==0 and maps[ni][nj] != 'X':
                                v[ni][nj]^=1
                                cnt += int(maps[ni][nj])
                                q.append((ni,nj))
                    answer.append(cnt)
    answer.sort()
    return answer if answer else [-1]