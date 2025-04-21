from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    directions = [[-1,0], [0, 1], [1, 0], [0, -1]]
    
    # 방문 저장 
    visited = [ [ False for _ in range(m)] for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]
    
    # 석유 덩어리 번호 : 개수  
    info = {0 : 0}
    num = 1 
    
    for j in range(m):
        for i in range(n):
            if visited[i][j] :
                continue
            if land[i][j] == 0 :
                continue
            
            # 방문 하지 않은 석유 덩어리 발견 
            queue = deque()
            queue.append([i,j])
            visited[i][j] = True
            check[i][j] = num
            cnt = 1 
            
            while queue : 
                x, y = queue.popleft()
                for dx , dy in directions : 
                    nx = x + dx
                    ny = y + dy
                    if (0<= nx < n) and (0<= ny < m) :
                        if land[nx][ny] == 1 and (visited[nx][ny] == False):
                            visited[nx][ny] = True
                            check[nx][ny] = num
                            cnt +=1
                            queue.append([nx,ny])
            info[num] = cnt
            num +=1
    
    answer = 0 

    for j in range(m) :
        temp = set()
        
        for i in range(n):
            if (check[i][j] > 0):
                temp.add(check[i][j])
                
        
        if (len(temp) > 0):
            req = sum([info[c] for c in temp])
            answer = max(answer, req)
        
                        
    return answer