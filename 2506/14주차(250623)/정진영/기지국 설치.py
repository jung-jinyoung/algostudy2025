def solution(n, stations, w):    
    
    now = 1 # 검사하려는 아파트 위치
    i = 0 # 기지국이 설치된 리스트 인덱스 
    answer = 0
    while now  <= n :
        # 현재 위치가 설치된 기지국에 커버 가능 할 경우
        if i < len(stations) and stations[i] - w <= now <= stations[i] + w :
            # 기지국 설치 x
            now = stations[i] + w + 1
            i += 1
        else : 
            # 최대 커버 할 수 있는 위치에 기지국 설치 O
            answer += 1
            now += 2*w + 1

    return answer