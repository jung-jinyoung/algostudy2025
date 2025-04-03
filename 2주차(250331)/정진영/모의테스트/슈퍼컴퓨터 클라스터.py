import sys

input = sys.stdin.readline

n, b = map(int, input().split())
arr = list(map(int, input().split()))
# 오름차순 정렬
arr.sort()

# 매개 변수 설정 : 최소값과 최대값 (성능)

left, right = 1, 2*10**9

# x 값을 최소성능이라 설정했을 때의 cost 비교 
def test(x):
    cost = 0
    for i in range(n):
        if arr[i] < x :
            cost += (x - arr[i]) ** 2
    
    return cost <= b

# 이진 탐색
while left < right : 
    ## 무한 루프 발생 방지
    mid = (left + right + 1) // 2
    # 예산 가격 미만 시 하향값 갱신
    if test(mid) : left = mid
    # 예산 가격 초과 시 상향값 갱신
    else : right = mid - 1

print(left)
