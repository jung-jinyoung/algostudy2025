import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    left = 0 
    right = n - 1

    # right 600 초과: count +1 , 왼쪽으로 이동 
    while left <= right and arr[right] > 600 :
        count +=1
        right -=1
        
    # 300 + 600 일 경우
    while left < right and arr[left] == 300 and arr[right] == 600:
        count +=1
        left += 1
        right -=1
        
    # left가 300일 경우 cnt_300 +=1 (세개를 한 서버 안에 넣으면 최적)
    cnt_300 = 0
    while left <= right and arr[left] == 300 :
        cnt_300 +=1
        left +=1
        
    # 301~600 경우의 수 확인 
    while left < right :
        if arr[left] + arr[right] <= 900:
            left +=1
            right -=1
            count +=1
        # 사용할 수 있는 300의 개수가 남아 있다면 서버 증설
        elif cnt_300 > 0 :
            cnt_300 -=1 
            right -=1
            count +=1
        # 서버 증설
        else :
            right -=1
            count+=1
    # 하나 남았을 경우 처리
    if left == right :
        if cnt_300 > 0 :
            cnt_300 -=1
        count +=1
    # 300 남은 개수 처리 
    count += cnt_300 // 3
    # 3으로 떨어지지 않을 경우 서버 증설
    if cnt_300 % 3 != 0:
        count += 1

    print(count)
            
            