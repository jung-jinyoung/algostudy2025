from collections import deque
def solution(maps):
    answer = []
    maps = list(map(list, maps))
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    def bfs(a, b):
        q = deque()
        food = 0
        q.append((a,b))
        visited[a][b] = 1
        food += int(maps[a][b])
        while q:
            i, j = q.popleft()
            # if visited[i][j] == 0:
            #     visited[i][j] = 1
            #     food += int(maps[i][j])
            for r in range(4):
                ni = i + di[r]
                nj = j + dj[r]
                if (0<=ni<len(maps)) and (0<=nj<len(maps[0])) and maps[ni][nj] != "X" and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    food += int(maps[ni][nj])
                    visited[ni][nj] = 1
        return food
    
    for a in range(len(maps)):
        for b in range(len(maps[0])):
            if visited[a][b] == 0 and maps[a][b] != "X":
                answer.append(bfs(a, b))
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer