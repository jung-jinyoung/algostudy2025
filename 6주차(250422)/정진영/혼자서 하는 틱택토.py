def check(arr):
    rows = [0, 0, 0]
    cols = [0, 0, 0]
    for (i, j) in arr:
        rows[i] += 1
        cols[j] += 1
        
    if 3 in rows or 3 in cols :
        return True
    # 대각선 
    check = [[(0,0),(1,1),(2,2)], [(0,2), (1,1), (2,0)]]
    for c in check:
        temp = 0
        for pos in c:
            if pos in arr:
                temp +=1
            else :
                break
        if temp == 3:
            return True
    return False
        
    

def solution(board):
    arr_O = []
    arr_X = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                arr_O.append((i, j))
            elif board[i][j] == "X":
                arr_X.append((i, j))
    # 안되는 경우
    ### 한쪽 개수가 1보다 더 많을 경우
    if len(arr_O) - len(arr_X) > 1 or len(arr_X) > len(arr_O):
        return 0

    check_O = check(arr_O)
    check_X = check(arr_X)
    
    
    ### X나 O가 빙고인데 상대쪽 카운트보다 작거나 같을경우
    if check_O and len(arr_O) != len(arr_X) + 1 :
        return 0
    if check_X and len(arr_X) != len(arr_O) :
        return 0
     
    
    if check_O and check_X:
        return 0

    
    return 1