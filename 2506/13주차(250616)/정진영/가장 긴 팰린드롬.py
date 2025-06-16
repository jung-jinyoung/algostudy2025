# 팰린드롬 확인 : 가운데 문자열을 중심으로 양 옆 확인
# -> 1. 짝수 길이인 경우 자기 자신과 그 다음 문자 기준 : 카운트 0
# -> 2. 홀수 길이인 경우 자기 자신이 중심 문자 : 카운트 1
def solution(s):
    l = len(s)
    # 정답 초기화 
    answer = 0
    
    def check(start, end, count) : 
        while (0<= start) and (end < l):
            if s[start] == s[end]:
                count +=2
                start -= 1
                end +=1
            else:
                break
        return count 
                    

    for i in range(l):
        # 짝수 길이 확인 :i, i+1, 0
        temp1 = check(i, i+1, 0)
        # 홀수 길이 확인 : i-1~ i+1, 1
        temp2 = check(i-1, i+1, 1)
        answer= max(answer, temp1, temp2)
        
    return answer