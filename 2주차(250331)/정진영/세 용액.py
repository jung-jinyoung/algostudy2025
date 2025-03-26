import sys
from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

# 투포인터 조회를 위한 오름차순 정렬
arr.sort()

def func(arr, n):
    answer = []
    result = float("inf")

    for i in range(n-2):
        pick = arr[i]
        # 이후 배열에서 선택할 용액 찾기 
        left = i+1
        right = n-1
        
        while left < right :
            check = pick + arr[left] + arr[right]
            if (check == 0) :
                answer = [i, left, right]
                return answer
            
            if abs(check) < result :
                result = abs(check)
                answer = [i, left, right]
            
            if (check < 0):
                left +=1
            else:
                right -=1
    
    return answer

answer = func(arr, n)
print(*[arr[i] for i in answer])
        