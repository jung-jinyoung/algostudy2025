## 2025.06.02 테스트케이스 (3/7 성공)
### 접근 방법
### 1. 초침, 분침, 시침의 각도를 계산한다.
### 2. 각도를 비교하여 겹쳤을 경우 +1 
### 3. 시간 단위는 초 단위로 진행 


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 현재 시간의 각도 계산
    def get_angles(h, m, s):
        sa = s * 6  # 초침
        ma = (m + s / 60) * 6  # 분침
        ha = (h % 12 + m / 60 + s / 3600) * 30  # 시침
        return sa, ma, ha

    # 각도 비교 함수 (360도 기준 오차 허용)
    def check(a1, a2):
        diff = abs(a1 - a2)
        return diff < 1e-9 or abs(360 - diff) < 1e-9

    # 시간 범위 (초 단위)
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    for t in range(start, end + 1):
        h = t // 3600
        m = (t % 3600) // 60
        s = t % 60

        sa, ma, ha = get_angles(h, m, s)

        # 각 경우별로 따로 카운트
        if check(sa,ha) or check(sa, ma) :
            answer+=1 
        
    
    return answer
