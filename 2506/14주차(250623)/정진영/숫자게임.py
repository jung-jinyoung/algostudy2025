from heapq import heappush, heappop, heapify
def solution(A, B):
    # A의 최소 점수가 B 최대 점수보다 같거나 높을 경우 0
    if min(A) >= max(B) :
        return 0
    A.sort()
    B.sort()
    heapify(B)
    i = 0 # 정렬한 A 리스트 인덱스 
    answer = 0
    while i < len(A) and len(B) > 0:
        a = A[i]
        b = heappop(B)
        if a < b : 
            answer +=1 
            i+=1
            continue
        
            
    return answer