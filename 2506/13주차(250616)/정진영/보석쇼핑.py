## 2025.06.16 (31.1% / 0.0%) : 완전 탐색 접근 -> 시간 초과

def solution(gems):
    jewels = set(gems)
    # for l in range(len(jewels), len(gems)+1):
    answer = []
    length = len(gems) + 1
    
    for i in range(len(gems)):
        if length == len(jewels) : 
            break
        l = len(jewels)
        while l <= len(gems) and l < length:
            check =  jewels -  set(gems[i:i+l])
            if len(check) == 0:
                if l < length :
                    answer = [i+1, i+l]
                    length = l
                    break
            else : 
                l += len(check)
    return answer