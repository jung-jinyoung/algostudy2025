# [근무 태도 점수 , 동료 평가 점수]
## 정렬 1. 근무태도 내림차순 -> 정렬 2. 동료평가 오름차순
### 동료평가 점수가 이전보다 작다면 ? -> 제외 
#### 결론 : 완호 앞에 몇명이 있는지 count 
    
def solution(scores):
    
    answer = 1
    # 완호 점수 
    target = scores[0]
    # 정렬 
    scores.sort(key = lambda x : (-x[0], x[1]))
    
    max_score = 0 # 동료 점수 최대값 초기화
    
    for score in scores:
        # 완호보다 둘 다 높을 경우 : 완호 -> 인센티브 대상 아님 
        if score[0] > target[0] and score[1] > target[1] :
            return -1
        # 인센티브 받을 수 있는 대상만 확인
        if score[1] >= max_score:
            if sum(score) > sum(target):
                answer +=1
            max_score = max(max_score, score[1]) # 최대값 갱신
    
    return answer 