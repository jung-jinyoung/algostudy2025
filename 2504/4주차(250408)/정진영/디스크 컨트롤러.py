## 우선순위 디스크 컨트롤러
# 1. 요청 시각이 빠른 것 부터 디스크 컨트롤러에 추가
## 2. 디스크 컨트롤러 확인 :  요청 시각이 실행 시간보다 작거나 같을 경우 소요시간이 작은 순서대로 
### 3. 모두 jobs 조회 후 디스크 컨트롤러 확인 -> 요청 작업이 남아있으면 추후 처리
from heapq import heapify, heappush, heappop

def solution(jobs):
    result = 0 
    now = 0 # 현재 시각
    n  = len(jobs) # 요청된 작업의 양
    heapify(jobs)
    # 요청 중인 작업 처리 힙
    h  = [] 
    while (jobs) :  
        while (True):
            # 현재 시각보다 이전에 요청된 모든 작업 저장 
            if len(jobs) > 0 and jobs[0][0] <= now :
                t, c = heappop(jobs)
                
                # 임시 힙에 저장
                # 저장 순서 : 소요 시각 기준 최소 힙 
                heappush(h, [c, t])
            else : 
                # 없으면 중지
                break
        
        # 현재 요청 시각 이전에 이력이 있으면 처리 
        if len(h) > 0 :
            c, t = heappop(h)
            # 작업 종료 시각 - 요청 시각 추가
            end = now + c
            result += end - t
            # 현재 시각 갱신
            now = end 
        # 요청이력이 없으면 최근에 요청으로 갱신
        else : 
            t, c = heappop(jobs)
            end = t + c
            result += end - t
            # 현재 시각 갱신 
            now = end 
    
    # 나머지 처리
    while (h) :
        c, t = heappop(h)
        end = now + c
        result += end - t
        now = end 
        

    
    return result // n