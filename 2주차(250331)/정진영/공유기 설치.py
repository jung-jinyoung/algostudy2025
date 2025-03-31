import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
# 이분 탐색을 위한 정렬
arr.sort()

# 최소 거리와 최대 거리 초기화
min_dist = 1
max_dist = arr[-1] - arr[0]
# 정답 초기화
answer = 0

while min_dist <= max_dist :
    mid_dist = (min_dist + max_dist) // 2
    
    now = arr[0] # 첫번째 집엔 무조건 설치
    check = 1
    
    for i in range(1, n):
        # 거리 확인 후 해당되면 설치
        if (arr[i] - now >= mid_dist):
            check +=1
            # 설치 장소 갱신
            now = arr[i]
            
    if (check >= c) :
        min_dist = mid_dist + 1
        answer = mid_dist
    else : 
        max_dist = mid_dist - 1

print(answer)
    
    
    
    