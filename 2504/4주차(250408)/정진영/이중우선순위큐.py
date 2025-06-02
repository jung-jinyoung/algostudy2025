from collections import deque
from heapq import heappush, heappop

def solution(operations):
    # 이중 우선 순위 큐 생성 
    min_h = []
    max_h = []
    ## 동기화를 위한 방문 딕셔너리 생성
    visited = {}
    for ops in operations : 
        op, num = ops.split(" ")
        # 삽입
        if (op == "I"):
            heappush(min_h, (int(num)))
            heappush(max_h, (-int(num)))
            visited[int(num)] = visited.get(int(num), 0) + 1
        else:
            # 최댓값 삭제
            if (int(num) == 1 and max_h) :
                while max_h:
                    max_val = -heappop(max_h)
                    if( visited.get(max_val, 0) > 0) :
                        visited[max_val] -= 1
                        break
            elif (int(num) == -1 and min_h) :
                while min_h:
                    min_val = heappop(min_h)
                    if (visited.get(min_val, 0) > 0) :
                        visited[min_val] -= 1
                        break
    ## 최종적으로 남아있는 값 찾기            
    while min_h and visited.get(min_h[0], 0) == 0 :
        heappop(min_h)
    
    while max_h and visited.get(-max_h[0], 0) == 0:
        heappop(max_h)
    
    if (min_h and max_h) :
        return [-max_h[0], min_h[0]]
    else:
        return [0, 0]
        